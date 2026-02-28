from typing import Dict, Any, AsyncGenerator
import aiohttp
from pydantic import ValidationError

from tgwallet.types.enums import CryptoCurrency, FiatCurrency, TradeSide
from tgwallet.models.models import (
    GetOnlineItemsRequestBody,
    GetOnlineItemsResponse,
    ErrorResponse, Item,
)
from tgwallet.exceptions import APIError, APIValidationError


class WalletP2PClient:
    BASE_URL = "https://p2p.walletbot.me"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.session: aiohttp.ClientSession | None = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=15)
        )
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def _make_request(
        self,
        method: str,
        path: str,
        json_data: Dict[str, Any] | None = None
    ) -> Dict[str, Any]:

        if not self.session:
            raise RuntimeError("Client must be used in async context manager")

        url = f"{self.BASE_URL}{path}"

        headers = {
            "X-API-Key": self.api_key,
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        async with self.session.request(
            method,
            url,
            headers=headers,
            json=json_data
        ) as response:

            data = await response.json()

            if response.status != 200:
                try:
                    error = ErrorResponse.model_validate(data)
                    raise APIError(
                        code=error.error_code,
                        status=response.status,
                        message=error.error_message,
                    )
                except ValidationError:
                    raise APIError(
                        error_code="UNKNOWN_ERROR",
                        message=str(data),
                        status_code=response.status
                    )

            return data

    async def get_online_items(
        self,
        request_body: GetOnlineItemsRequestBody
    ) -> GetOnlineItemsResponse:

        path = "/p2p/integration-api/v1/item/online"
        raw = await self._make_request(
            "POST",
            path,
            request_body.model_dump(by_alias=True)
        )

        try:
            return GetOnlineItemsResponse.model_validate(raw)
        except ValidationError as e:
            raise APIValidationError(str(e)) from e

    async def get_sell_items(
            self,
            crypto: CryptoCurrency = CryptoCurrency.USDT,
            fiat: FiatCurrency = FiatCurrency.UAH,
            limit: int = 50,
    ) -> AsyncGenerator[Item, None]:

        page_size = 50  # максимум API
        page = 1
        yielded = 0

        while True:
            request_body = GetOnlineItemsRequestBody(
                crypto_currency=crypto,
                fiat_currency=fiat,
                side=TradeSide.SELL,
                page=page,
                page_size=page_size,
            )

            response = await self.get_online_items(request_body)

            if not response.data:
                break

            for item in response.data:
                yield item
                yielded += 1

                if yielded >= limit:
                    return

            if len(response.data) < page_size:
                break

            page += 1

    async def get_buy_items(
        self,
        crypto: CryptoCurrency = CryptoCurrency.USDT,
        fiat: FiatCurrency = FiatCurrency.UAH,
        limit: int = 50,
    ) -> AsyncGenerator[Item, None]:

        page_size = 50  # максимум API
        page = 1
        yielded = 0

        while True:
            request_body = GetOnlineItemsRequestBody(
                crypto_currency=crypto,
                fiat_currency=fiat,
                side=TradeSide.BUY,
                page=page,
                page_size=page_size,
            )

            response = await self.get_online_items(request_body)

            if not response.data:
                break

            for item in response.data:
                yield item
                yielded += 1

                if yielded >= limit:
                    return

            if len(response.data) < page_size:
                break

            page += 1

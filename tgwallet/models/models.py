from typing import List
from pydantic import BaseModel, Field, ConfigDict

from tgwallet.types.enums import TradeSide, ResponseStatus, ErrorCode, FiatCurrency, CryptoCurrency, MerchantLevel


# -------------------- REQUEST --------------------

class GetOnlineItemsRequestBody(BaseModel):
    """Request body for getting online items (ads)."""

    crypto_currency: CryptoCurrency = Field(alias="cryptoCurrency")
    fiat_currency: FiatCurrency = Field(alias="fiatCurrency")
    side: TradeSide

    page: int = 1
    page_size: int = Field(default=10, alias="pageSize")

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)


# -------------------- SUCCESS RESPONSE --------------------

class Item(BaseModel):
    """Model for a single online item (ad) in the response."""

    id: int
    number: str
    user_id: int = Field(alias="userId")
    nickname: str

    crypto_currency: CryptoCurrency = Field(alias="cryptoCurrency")
    fiat_currency: FiatCurrency = Field(alias="fiatCurrency")
    side: TradeSide

    price: str
    last_quantity: str = Field(alias="lastQuantity")
    min_amount: str = Field(alias="minAmount")
    max_amount: str = Field(alias="maxAmount")

    payments: List[str]

    order_num: int = Field(alias="orderNum")
    execute_rate: str = Field(alias="executeRate")

    is_online: bool = Field(alias="isOnline")
    merchant_level: MerchantLevel = Field(alias="merchantLevel")

    payment_period: int | None = None
    is_auto_accept: bool = Field(alias="isAutoAccept")

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)


class GetOnlineItemsResponse(BaseModel):
    """Response for getting online items (ads)."""
    status: ResponseStatus
    data: List[Item]


# -------------------- ERROR RESPONSE --------------------

class ErrorResponse(BaseModel):
    """Model for error responses"""
    error_code: ErrorCode = Field(alias="errorCode")
    error_message: str = Field(alias="errorMessage")

    model_config = ConfigDict(populate_by_name=True, use_enum_values=True)
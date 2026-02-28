# tgwallet

Async Python client for Telegram Wallet P2P Market API.

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Error Handling](#error-handling)
- [Official API Documentation](#official-api-documentation)
- [License](#license)


## Installation

```bash
pip install git+https://github.com/EntireMusic/tgwallet.git
```
---

## Quick Start

```python
import asyncio
from tgwallet import WalletP2PClient

async def main():
    async with WalletP2PClient(api_key="YOUR_API_KEY") as client:
        async for item in client.get_buy_items(limit=10):
            print(item)

asyncio.run(main())
```


## Error Handling

```python
from tgwallet import WalletP2PClient
from tgwallet.exceptions import APIError

try:
    ...
except APIError as e:
    print(e)
```

---

## Official API Documentation

This library is a wrapper around the official Telegram [Wallet P2P API](https://docs.wallet.tg/p2p)

---

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

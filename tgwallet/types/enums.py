from enum import Enum


class TradeSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


class CryptoCurrency(str, Enum):
    BTC = "BTC"
    ETH = "ETH"
    NOT = "NOT"
    TON = "TON"
    USDT = "USDT"


class FiatCurrency(str, Enum):
    USD = "USD"  # US Dollar
    EUR = "EUR"  # Euro

    AED = "AED"  # UAE Dirham
    AMD = "AMD"  # Armenian Dram
    AZN = "AZN"  # Azerbaijan Manat
    BRL = "BRL"  # Brazilian Real
    BYN = "BYN"  # Belarusian Ruble
    CZK = "CZK"  # Czech Koruna
    GBP = "GBP"  # British Pound
    GEL = "GEL"  # Georgian Lari
    IDR = "IDR"  # Indonesian Rupiah
    INR = "INR"  # Indian Rupee
    KGS = "KGS"  # Kyrgyzstani Som
    KZT = "KZT"  # Kazakhstani Tenge
    PHP = "PHP"  # Philippine Peso
    PLN = "PLN"  # Polish Zloty
    RUB = "RUB"  # Russian Rubli
    THB = "THB"  # Thai Baht
    TRY = "TRY"  # Turkish Lira
    UAH = "UAH"  # Ukrainian Hryvnia
    UZS = "UZS"  # Uzbekistani Som
    VND = "VND"  # Vietnamese Dong


class MerchantLevel(str, Enum):
    REGULAR_USER = "REGULAR_USER"
    MERCHANT = "MERCHANT"
    TRUSTED_MERCHANT = "TRUSTED_MERCHANT"


class ResponseStatus(str, Enum):
    SUCCESS = "SUCCESS"


class ErrorCode(str, Enum):
    CRYPTO_CURRENCY_NOT_SUPPORTED = "CRYPTO_CURRENCY_NOT_SUPPORTED"
    FIAT_CURRENCY_NOT_SUPPORTED = "FIAT_CURRENCY_NOT_SUPPORTED"
    ACCESS_DENIED = "ACCESS_DENIED"
    INTERNAL_ERROR = "INTERNAL_ERROR"
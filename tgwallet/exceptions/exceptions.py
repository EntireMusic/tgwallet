from tgwallet.types.enums import ErrorCode


class WalletP2PError(Exception):
    """Base SDK exception."""


class APIError(WalletP2PError):
    """API returned structured error."""

    def __init__(self, status: int, code: ErrorCode, message: str):
        self.code = code
        self.status = status
        self.message = message
        super().__init__(f"{status} {code.value}: {message}")


class APIValidationError(WalletP2PError):
    """Response schema mismatch."""
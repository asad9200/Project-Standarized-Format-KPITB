"""Shared platform exception types."""


class PlatformError(Exception):
    """Base error for the platform."""


class ConfigurationError(PlatformError):
    """Raised when settings are missing or invalid."""

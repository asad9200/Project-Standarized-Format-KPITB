"""Startup, shutdown, and resource lifecycle management."""
from core.logging import get_logger

logger = get_logger(__name__)


def startup() -> None:
    logger.info("Platform starting up")


def shutdown() -> None:
    logger.info("Platform shutting down")

"""Platform entry point: initializes and launches selected apps.

Usage:
    python main.py              # list available apps
    python main.py app1         # run one app
    python main.py app1 app2    # run several apps
"""
import importlib
import sys

from core.config import settings
from core.lifecycle import shutdown, startup
from core.logging import get_logger

logger = get_logger(__name__)

# Register every app here: short name -> module path
APPS = {
    "app1": "Apps.App1.main",
    "app2": "Apps.App2.main",
}


def run_app(name: str) -> None:
    module = importlib.import_module(APPS[name])
    module.run()


def main(selected: list[str]) -> None:
    if not selected:
        print("Available apps:", ", ".join(APPS))
        return
    unknown = [n for n in selected if n not in APPS]
    if unknown:
        sys.exit(f"Unknown app(s): {', '.join(unknown)}")

    startup()
    try:
        for name in selected:
            logger.info("Starting %s (%s)", name, settings.environment)
            run_app(name)
    finally:
        shutdown()


if __name__ == "__main__":
    main(sys.argv[1:])

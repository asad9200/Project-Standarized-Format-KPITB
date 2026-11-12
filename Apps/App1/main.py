"""Builds and starts App1's components."""
from Apps.App1.config.settings import settings
from Apps.App1.helper import greeting


def run() -> None:
    print(greeting(settings.app_name))


if __name__ == "__main__":
    run()

"""Builds and starts App2's components."""
from Apps.App2.config.settings import settings
from Apps.App2.helper import greeting


def run() -> None:
    print(greeting(settings.app_name))


if __name__ == "__main__":
    run()

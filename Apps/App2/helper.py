"""Helper functions used within App2 only.

If a helper is needed by another app too, move it to shared/utilities/.
"""


def greeting(app_name: str) -> str:
    return f"{app_name} is running."

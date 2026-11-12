from Apps.App1.helper import greeting


def test_greeting():
    assert greeting("App1") == "App1 is running."

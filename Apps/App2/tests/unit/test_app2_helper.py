from Apps.App2.helper import greeting


def test_greeting():
    assert greeting("App2") == "App2 is running."

import main


def test_all_registered_apps_run():
    for name in main.APPS:
        main.run_app(name)

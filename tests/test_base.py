from pytest import fixture, mark


@mark.usefixtures("chrome_browser")
class BaseTests:
    pass

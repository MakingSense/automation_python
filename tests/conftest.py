from pytest import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Config import Config

# function -> one webdriver instace per tests case (function)
# Session -> one webdriver for every tests

# This method is to set up a chome driver using ChromeDriverManager
# If a different browser is required it can be set here



@fixture(scope='class')
def chrome_browser(request):
    web_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = web_driver
    yield
    web_driver.close()

# This method can be used to set up different environments in which the tests can be run
# The environments can be set in the Config.py file
@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")

# This is retriving the information set in the Config.py file
@fixture(scope='session')
def app_config():
    return Config()

# This method is used to execute the tests in the command line mentioning the environment in which the tests must be run
def pytest_addoption(parser):
    parser.addoption("--env", action="store", help="Environment to run tests against")

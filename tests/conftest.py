import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


# @pytest.fixture(params=["chrome", "firefox"])
@pytest.fixture
# Fixture is a prepared environment that can be used for a test execution.
# We use fixtures to make test setup easier and isolated from the test functions. Simple example: preparation of a Python list.
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"creating {browser} driver")
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")
    #my_driver.implicitly_wait(10)

    yield my_driver
    # everything that goes after YIELD will be executed after all the tests are run
    # my_driver.close() # closes the tab, not the whole window
    print(f"closing {browser} driver")
    my_driver.quit()
    # a built-in function that ends the execution of a Python program. It's a straightforward way to stop a program.


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox)"
    )

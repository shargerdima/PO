from selenium.webdriver import Chrome
import pytest

@pytest.fixture(scope="function")
def browser():
    browser = Chrome('/Users/pepa-pcx/drivers/chromedriver_mac')
    yield browser
    browser.close()

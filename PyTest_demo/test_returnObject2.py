import pytest

import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Initialize the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()  # You can configure the path to the driver executable if needed
    yield driver  # Provide the driver to the test
    driver.quit()  # Cleanup after the test



@pytest.mark.usefixtures("driver")
class TestExample:
    # Use the driver fixture in a test method
    def test_open_google(self, driver):
        driver.get("https://www.google.com")
        assert "Google" in driver.title

    # Another example of using the driver in a class method
    def test_open_bing(self, driver):
        driver.get("https://www.bing.com")
        assert "Bing" in driver.title











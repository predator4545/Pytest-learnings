import pytest
from selenium import webdriver


@pytest.fixture
def driver():  #The driver() function is a fixture that sets up and returns a WebDriver instance.
    # Initialize the WebDriver (e.g., ChromeDriver)
    driver = webdriver.Chrome()

    # Optional: Set driver options or configurations here
    driver.maximize_window()

    # Provide the driver object to the test
    yield driver   #The yield statement provides the driver object to the test function.
    #when a fixture uses yield, it allows you to set up a resource (e.g., a driver object) before the test and clean it up afterward.
    #It doesn't inherently assign the driver to a class variable unless you explicitly code it that way.
    #In this example:
    #The driver() fixture sets up the driver object, yields it to the test, and ensures proper cleanup afterward.
    #yield driver simply makes the driver object available to the test function; it doesn’t assign it to a class variable.


    # Cleanup: Close the browser after the test
    driver.quit()   #After the test is complete, driver.quit() is called to close the browser and free resources.



class TestExample:    #Test classes must be named “Test”
   def test_google_search(self, driver):  #The test_google_search function accepts the driver fixture as an argument. The driver is automatically passed by pytest.
       # Use the driver object
       driver.get("https://www.example.com")
       assert "Example Domain" in driver.title

   def test_open_bing(self, driver):
       driver.get("https://www.bing.com")
       assert "Bing" in driver.title





@pytest.fixture(params=["chrome", "firefox"]) #This allows you to run the test with multiple browsers by parameterizing the fixture.
def driverB(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {request.param}")

    yield driver
    driver.quit()

# Test function
def test_example(driverB):
    driverB.get("https://example.com")
    assert "Example" in driverB.title
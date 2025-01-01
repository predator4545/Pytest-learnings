import pytest
from selenium import webdriver

#If you'd like to return a Selenium driver object to a class instead of a method in pytest, you can assign it to a class variable during setup. This is useful if you want the driver to be shared across all the methods in the class and accessed via self or the class name.

#Below is an example of how to achieve this in pytest:

@pytest.fixture(scope="class")
def driverA():
    # Setup: Create the driver instance
    driver = webdriver.Chrome()
    yield driver  # Yield the driver object for use in tests
    # Teardown: Quit the driver after all tests
    driver.quit()


@pytest.mark.usefixtures("driverA")
class TestExample:
    # Class variable to hold the driver
    driver = None

    @pytest.fixture(autouse=True, scope="class")
    def setup_class_driver(self, driverA):
        # Assign the driver fixture to the class variable
        TestExample.driver = driverA
        #Class-Level Assignment via Fixture:
        #Use an @pytest.fixture with autouse=True to assign driverA to self.driver at the class level.



    #pytest.fixture(autouse=True, scope="class")              autouse helps to use this function automatically, no need to make it as a individual method using test keyword
    #def test_setup_class_driver(self, driverA):
    #    # Assign the driver fixture to the class variable
    #    TestExample.driver = driverA                          using self.driver is not working, so stick to class name.driver
                                                               #In pytest, each test method is executed independently, so self.driver will not persist across tests
    def test_open_google(self):
        # Use the class-level driver
        TestExample.driver.get("https://www.google.com")
        assert "Google" in TestExample.driver.title

    def test_open_example(self):
        # Use the same class-level driver
        TestExample.driver.get("https://www.example.com")
        assert "Example" in TestExample.driver.title


#Question :  why TestExample.driver is working and self.driver is not working

#1. Class Context in setup_class_driver

#In the setup_class_driver fixture, self refers to the instance of the test class (TestExample).
#However, when you assign a value to self.driver inside the fixture,
# it won't persist across test methods because pytest creates a new instance of the test class for each test method.
# This means self.driver will be reset for every test

#def setup_class_driver(self, driverA):
#    self.driver = driverA  # Assign to self.driver

#In this case:

#self.driver is only valid within the scope of that particular instance.
#When pytest moves to the next test method, it creates a new instance of TestExample,
# and self.driver will no longer have the value assigned in setup_class_driver.

#2. Class Variable (TestExample.driver)
#To ensure that the driver is shared across all test methods,
# you use a class variable like TestExample.driver.
# Class variables are shared across all instances of the class,
# which solves the problem of pytest creating new instances for each test method.


#3. Why self.driver Works Inside Tests
#In the test methods themselves, you use self.driver to access the driver.
# This works because Python first checks for an instance variable (self.driver) and,
# if not found, looks for a class variable (TestExample.driver).
# Since the driver was set as a class variable, self.driver resolves to TestExample.driver.


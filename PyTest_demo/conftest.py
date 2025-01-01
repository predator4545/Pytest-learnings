#fixtures are used for setup and tear down method for tc's - conftest file to generalize
#fixture and make it available to all tests
#conftest is the exact keyword we need to use to create the file
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service




#since we are declaring fixture in conftest file, this fixture method will be available for all pytest test files
@pytest.fixture(scope="class")    #scope = "class" is added, so this fixture will run only once, not for every methods in class            #
def setup():
    print("need to be executed as first")
    yield    # yield will wait for other methods to complete before getting into below statement
    print("will run at last")


@pytest.fixture(scope="class")
def dataLoad():
    print("user profile data has been created")
    return ["Rahul","shetty","rahulshetty@gmail.com"]

@pytest.fixture(params=[["mahesh","23"],["bala","20"],["selva",24]])    #params used to pass multiple datas
def MultipleDataLoad(request):   #request will take one data at a time and will pass, request will be used only when params is used
    return request.param

#to generate html report for pytest, use-->pip install pytest-html    to install in cmd
# then to generate a report enter ---->python -m pytest --html=report.html
#now u could find the report in the same path as pytest/ in pychar IDE too





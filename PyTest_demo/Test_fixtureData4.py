import pytest
from selenium.webdriver.common.by import By
from PyTest_demo.conftest import dataLoad
from PyTest_demo.loggerClass import LoggerClass
from selenium import webdriver
#never forgot to start method with test
@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editProfile(self,dataLoad):  #dataLoad is added here to catch the returned value from fixture
        print(dataLoad)

@pytest.mark.usefixtures("MultipleDataLoad")
class TestMultiple(LoggerClass):  #inherit LoggerClass to use its logger object and to pass logs

    def test_miltipleDataInput(self,MultipleDataLoad):
        print(MultipleDataLoad[1])
        log = self.getLogger()  #calling a function in a parent class which is returning logger object
        log.info(MultipleDataLoad[1])

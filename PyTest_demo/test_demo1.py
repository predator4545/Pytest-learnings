#Any Pytest file should start with test_ or end with_test keywords
#each methods/funtions is a different Test case
from calendar import different_locale

import pytest


#pytest method names start with test
#Any test code should be wrapped in method only

#----------using method names-----#

#we can also run using command prompt
#copy pytest folder path    cd C:\Users\Selvakumar\PycharmProjects\PythonProject\PyTest_demo---->py.test -v -s"""
# in our case we should use ----->python -m pytest -v -s( from python it will search for module named pytest and then it will run the files
#bz, python and pytest installed location are different, so we need to start with python since we are running python codes then search for module pytest and then need to execute the tc's
#if we need to run particular file. then use --->python -m pytest test_demo2.py -v -s
#we can also run particular set of Tc's according to their name  ------->python -m pytest -k CreditCard -v -s,   -k is a mandate before entering keyword attached in methods(CreditCard)
#-k stands for method names execution, -s logs in output -v stands for more info metedata


#U--------sing @pytest.mark keywords---------------------#

#WE can execute Group test cases using pytest mark, we can mark(tag) testcases like @pytest.mark.smoke(smoke can be replaced by any keyword eg.,regression etc.) and then run with -m in cmd --->python -m pytest -m smoke -v -s
#@pytest.mark.skip to skip particular Tc's---->python -m pytest -v -s

@pytest.mark.smoke
def test_firstProgram():
    print("Hello")
    #cannot run this code normally using Run option, even if we run, it will not give output
    #we might need to use edit configuration to run this page

@pytest.mark.skip
def test_secondProgram_CreditCard():
    print("Second Hello")


#Marks in pytest are a way to label or annotate test functions. They help organize, filter, and customize the behavior of tests. Marks are flexible and can be used for many purposes:

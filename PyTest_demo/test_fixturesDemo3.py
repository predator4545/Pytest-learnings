import pytest
#fixture is like @before @after in testNG
#Fixtures are used to provide setup and teardown for your tests, making them reusable and modular. They can be used to prepare test dependencies like data, configurations, or connections.

#the following function will only run after setup method is completed

#@pytest.fixture will declare the following method setup as a fixture method which can be called upon by any methods in this file( should pass fixture method name as a argument)
@pytest.fixture()
def maxFun():
    print("need to be executed as first")
    yield    # yield will wait for other methods to complete before getting into below statement
    print("will run at last")

def test_fixtureDemo(maxFun):  # calling fixture method
    print("will execute steps in fixture demo method")


#to avoid creating fixture for every file, we could generalize the existing fixture by putting it in a class under conftest file
#another fixture method is created in conftest file to generalize
#below method will look for setup fixture method in this file, if it is not present then it will for conftest file
def test_fixtureDemo(setup):  #calling fixture method in conftest file
    print("will execute steps in fixture demo method")

#in case of multiple tc's in one test file,
#if we declare all the methods under a class, we can declare fixture method din class level, so it will be automatically applied to all methods inside
#class created , by using usefixtures annotation, we will call fixture method


@pytest.mark.usefixtures("setup")  #setting connection with fixture method
class TestExample:
    def test_fixtureDemo(self): #changed from setup to self
        print("will execute steps in fixture demo method")

    def test_fixtureDemo1(self):
        print("will execute steps in fixture demo method")

    def test_fixtureDemo2(self):
        print("will execute steps in fixture demo method")

    def test_fixtureDemo3(self):
        print("will execute steps in fixture demo method")
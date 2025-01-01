import pytest

#xfail will run the TC but it won't show the result either pass or fail,


@pytest.mark.xfail
def test_thirdProgram_CreditCard():
    print("third Hello")


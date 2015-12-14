import pytest 
def func(x):
    return x + 1

@pytest.mark.webtest
def test_answer8():
    assert func(3) == 5

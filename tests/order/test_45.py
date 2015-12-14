import pytest

@pytest.mark.run(order=2)
def test_foo():
    print "foo"
    assert True

@pytest.mark.run(order=1)
def test_bar():
    assert True

@pytest.mark.run(order=1)
def test_qoo():
    assert True

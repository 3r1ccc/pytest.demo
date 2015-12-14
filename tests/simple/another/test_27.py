# content of test_module.py

import pytest


good = pytest.mark.skipif(
    not pytest.config.getoption("--rungood"),
    reason="need --rungood option to run"
)

slow = pytest.mark.skipif(
    not pytest.config.getoption("--runslow"),
    reason="need --runslow option to run"
)

def test_func_fast():
    pass


@slow
def test_func_slow():
    pass

@good 
def test_func_good():
    pass

@good
@slow
def test_func_nice():
    pass

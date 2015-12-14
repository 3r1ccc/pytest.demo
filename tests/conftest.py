# content of conftest.py
import pytest


def pytest_addoption(parser):
    parser.addoption("--cmdopt", action="store", default="type1",
        help="my option: type1 or type2")

    parser.addoption("--rungood", action="store_true",
        help="run good tests")

    parser.addoption("--runslow", action="store_true",
        help="run slow tests")




def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item

def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" %previousfailed.name)

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")


@pytest.fixture(scope="session", autouse=True)
def printsomething(request):
    print ("-start of session")
    def fin():
        print ("-end of session")
    request.addfinalizer(fin)
    return printsomething

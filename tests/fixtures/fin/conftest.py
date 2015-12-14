# content of conftest.py

import smtplib
import pytest

@pytest.fixture(scope="module")
def smtp3(request):
    smtp3 = smtplib.SMTP("smtp.gmail.com")
    def fin():
        print ("teardown smtp")
        smtp3.close()
    request.addfinalizer(fin)
    return smtp3  # provide the fixture value

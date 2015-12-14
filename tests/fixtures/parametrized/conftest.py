# content of conftest.py
import pytest
import smtplib

@pytest.fixture(scope="module",
                params=["smtp.gmail.com", "mail.python.org"])
def smtp6(request):
    smtp6 = smtplib.SMTP(request.param)
    def fin():
        print ("finalizing %s" % smtp6)
        smtp6.close()
    request.addfinalizer(fin)
    return smtp6

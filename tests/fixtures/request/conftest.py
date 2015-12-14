# content of conftest.py
import pytest
import smtplib

@pytest.fixture(scope="module")
def smtp4(request):
    server = getattr(request.module, "smtpserver", "smtp.gmail.com")
    smtp4 = smtplib.SMTP(server)

    def fin():
        print ("finalizing %s (%s)" % (smtp4, server))
        smtp4.close()
    request.addfinalizer(fin)
    return smtp4

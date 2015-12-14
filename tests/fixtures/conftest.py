# content of conftest.py
import pytest
import smtplib

@pytest.fixture(scope="module")
def smtp2():
    return smtplib.SMTP("smtp.gmail.com")

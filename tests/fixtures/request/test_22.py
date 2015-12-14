smtpserver = "mail.python.org"  # will be read by smtp fixture

def test_showhelo(smtp4):
    assert 0, smtp4.helo()

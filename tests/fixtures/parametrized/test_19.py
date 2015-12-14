# content of test_module.py

def test_ehlo(smtp6):
    response, msg = smtp6.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0  # for demo purposes

def test_noop(smtp6):
    response, msg = smtp6.noop()
    assert response == 250
    assert 0  # for demo purposes

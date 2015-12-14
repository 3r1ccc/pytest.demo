# content of test_module.py

def test_ehlo(smtp2):
    response, msg = smtp2.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0  # for demo purposes

def test_noop(smtp2):
    response, msg = smtp2.noop()
    assert response == 250
    assert 0  # for demo purposes

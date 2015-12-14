# content of test_module.py

def test_ehlo(smtp3):
    response, msg = smtp3.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0  # for demo purposes

def test_noop(smtp3):
    response, msg = smtp3.noop()
    assert response == 250
    assert 0  # for demo purposes

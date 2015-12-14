def test_foo(variables):
    assert variables['foo'] == 'bar'
    assert variables.get('bar') == 'foo'
    assert variables.get('missing') is None

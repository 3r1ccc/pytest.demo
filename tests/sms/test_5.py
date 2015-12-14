# content of test_tmpdir.py
import os, pytest
@pytest.mark.skipif("sys.version_info >= (2,0)")
def test_create_file2(tmpdir):
    p = tmpdir.mkdir("sub").join("hello.txt")
    p.write("content")
    assert p.read() == "content"
    assert len(tmpdir.listdir()) == 1

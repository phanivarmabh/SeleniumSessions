import pytest

def test_m1():
    assert "phani" == "phani"


def test_m2():
    a=3
    b=4
    assert a+1 == 4, "test failed"
    assert a == b, "test failed, a is not eq to b"


def test_m3():
    assert 1 == 2, "input numbers are not equal"


def test_login_fb():
    assert "admin"  ==  "admin"
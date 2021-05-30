import pytest

@pytest.mark.sample
def test_num():
    assert 100 == 100

@pytest.mark.sample
def test_char():
    assert "varma" == "Varma"

@pytest.mark.sample
def test_login():
    assert "admin" == "admin"

@pytest.mark.sample
def test_bool():
    assert True
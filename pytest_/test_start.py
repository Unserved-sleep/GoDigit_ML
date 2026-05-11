import pytest

#function based
def test_addition():
    assert 5 + 5 == 10

#class based
class TestAddition:
    def test_addition(self):
        assert 5 + 5 == 10


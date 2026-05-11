import sys
import pytest

@pytest.mark.skip(reason="not needed")
def test_feature():
    pass

@pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
class TestClass:
    def test_feature(self):
        """This test will not run under win32"""

@pytest.mark.xfail(reason="division by zero not handled yet")
def test_division_by_zero():
    assert 5 / 0 == 0

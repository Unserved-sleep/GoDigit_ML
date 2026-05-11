import pytest

#calc square of number
def square_number(num):
    return num ** 2

#parametrize decorator
@pytest.mark.parametrize("input_value, expected_output", [
    (2, 4),
    (-3, 9),
    (0, 0)
])

def test_square(input_value, expected_output):
    assert square_number(input_value) == expected_output
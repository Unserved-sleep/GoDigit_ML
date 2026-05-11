import pytest
import math

def calculate(val):
    if val < 0:
        raise ValueError("Value must be positive")
    return math.sqrt(val)

def test_calculate_square_root():
    with pytest.raises(ValueError):
        calculate(1)

def test_calculate_negative_square_root():
    with pytest.raises(ValueError):
        calculate(-1)

def divide_numbers(numerator, denominator):
     return numerator / denominator

def test_divide_numbers():
     with pytest.raises(ZeroDivisionError):
         divide_numbers(10, 0)

def add_numbers(a, b):
     return a + b

def test_add_numbers():
     with pytest.raises(TypeError):
         add_numbers("10", 5)
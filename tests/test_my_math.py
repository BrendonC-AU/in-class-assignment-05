import pytest

from src.my_math import sum, multiply, difference

def test_sum():
    res = sum(1,1)
    assert res == 2

# Work together
## Test multiply

def test_mult():
    res = multiply(2,2)
    assert res == 4


# Check for understanding
## Test difference

def test_diff():
    res = difference(2,1)
    assert res == 1


# Work together
## Test absolute sum



# Check for understanding
## Test calculate age

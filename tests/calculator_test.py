"""Testing the Calculator"""
# From specifies the namespace
from calculator import Calculator


def tuple_list():
    """Arranging Data for AAA Testing"""
    return 8.0, 2


def test_calculator_add_method():
    """Testing the Calculator add """
    # this is show using the calculator object add method

    ## Act for AAA testing
    result = Calculator.add(tuple_list())

    ## Assertion for AAA testing
    assert result == 10


def test_calculator_subtract_method():
    """Testing the Calculator Subtract"""
    assert Calculator.subtract(tuple_list()) == -10


def test_calculator_multiply_method():
    """Testing the Calculator multiply"""
    assert Calculator.multiply(tuple_list()) == 16

def test_calculator_divide_method():
    """Testing the Calculator multiply"""
    assert Calculator.divide(tuple_list()) == 0.0625

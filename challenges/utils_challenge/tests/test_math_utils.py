import pytest
from utils.math_utils import add_two_numbers, multiply_two_numbers

addition= [

     (2, 3, 5),  # positive integers
    (1, 99, 100),  # identity
    (0, 99, 99),  # zero
    (3, -4, -1),  # positive by negative
    (-5, -5, -10),  # negative by negative
]

products = [
    
    (2, 3, 6),  # positive integers
    (1, 99, 99),  # identity
    (0, 99, 0),  # zero
    (3, -4, -12),  # positive by negative
    (-5, -5, 25),  # negative by negative
    (2.5, 6.7, 16.75)  # float 

]

@pytest.mark.parametrize('a, b, sum', addition)
def test_add_two_numbers(a, b, sum):
    assert add_two_numbers(a , b) == sum

@pytest.mark.parametrize('a, b, product', products)
def test_multiply_two_numbers(a, b, product):
    assert multiply_two_numbers(a , b) == product


from utils.math_utils import add_two_numbers, multiply_two_numbers
from utils.string_utils import string_repeater as sr



add = add_two_numbers(2,2)
mult = multiply_two_numbers(5,5)
h = f'{sr("H", 1)}{sr("a", 1)}{sr("p",2)}{sr("y", 1)}'
b = f'{sr("B",1)}{sr("i",1)}{sr("t",1)}{sr("h", 1)}{sr("d",1)}{sr("a", 1)}{sr("y", 1)}{sr("!",10)}'
hb = f'{h} {b}'

print(f'2 + 2 = {add}')
print(f'5 * 5 = {mult}')
print(hb)

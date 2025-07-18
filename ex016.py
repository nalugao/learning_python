"""import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
print(f'A raiz de {num} é {math.ceil(raiz)}')"""

# Create a program that reads any real number from the keyboard and shows its integer part on the screen.
# Example: Enter a number: 5.400
# The number 5.400 has the integer part 5.

import math

n = float(input('Write a number: '))
i = math.trunc(n)
print(f'The integer part of the number {n} is {i}!')
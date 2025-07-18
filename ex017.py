# Write a program that reads the length of the opposite side and the adjacent side of a right triangle,
# calculates, and displays the length of the hypotenuse.

import math

# The square of the hypotenuse is equal to the sum of the squares of the two legs (the two shorter sides)

"""c1 = float(input('Write the length of the opposite side: '))
c2 = float(input('Write the length of the adjacent side: '))

c1sq = math.pow(c1, 2)
c2sq = math.pow(c2, 2)
h = math.sqrt(c1sq + c2sq)

print(f'The number {c1} squared is {c1sq:.2f}, and the for the number {c2}, is {c2sq:.2f}.\n '
      f'The sum of the sides squared is {c1sq + c2sq}. So the hypotenuse is {h:.2f}')
"""

#or

c1 = float(input('Write the length of the opposite side: '))
c2 = float(input('Write the length of the adjacent side: '))
h = math.hypot(c1, c2)
print(f'The Hypotenuse is {h:.2f}')

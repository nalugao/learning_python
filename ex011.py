# Write a program that reads the width and height of a wall in meters, calculates its area,
# and the amount of paint needed to paint it, knowing that one liter of paint covers 2 m².

width = float(input('Width (m): '))
height = float(input('Height (m): '))

area = width*height
paint = area/2

print(f'The area is {area} m², so you will need {paint} liters of paint to cover the wall.')
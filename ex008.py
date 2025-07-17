# Write a program that reads a value in meters and displays it
# converted to centimeters and millimeters.

n = float(input('Write a value in meters: '))

c = n*100
m = n*1000

print(f'The value {n:.0f} in centimeters is {c:.0f} cm and in millimeters is {m:.0f} mm.')
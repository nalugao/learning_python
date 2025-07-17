# Write a program that reads a number and displays its double, triple, and square root.

n = int(input('Write a number: '))
d = n**2
t = n**3
sr = n**(1/2)

print(f'The double of the number {n} is {d}, the triple is {t} and the square root is {sr:.2f}.')
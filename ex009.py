# Write a program that reads any integer and shows its multiplication table on the screen.

n = int(input('Write a number: '))

print(f'The multiplication table of the number {n} is:')

cont = 0
while cont <= 10:
    t = n*cont
    print(t)
    cont += 1

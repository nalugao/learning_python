# Write a program that reads any integer and shows its multiplication table on the screen.

#Using while
n = int(input('Write a number: '))

print(f'The multiplication table of the number {n} is:')
print("-"*12)
cont = 0
while cont <= 10:
    t = n*cont
    print(f' {n} x {cont} = {t} ')
    cont += 1
print("-"*12)
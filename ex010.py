# Create a program that reads how much money a person has in their wallet and shows how
# many Dollars they can buy. Consider US$1.00 = R$3.27.

real = float(input('How much real do you have? '))
dolar = real/5.59
change = real%5.59
print(f'With R$ {real:.2f}, you can buy US$ {dolar:.2f} and you will have R$ {change:.2f} left as change.')
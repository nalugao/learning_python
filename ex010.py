# Create a program that reads how much money a person has in their wallet and shows how
# many Dollars they can buy. Consider US$1.00 = R$3.27.

money = float(input('How much money do you have? '))
convert_money = money//5.59
change = money%5.59
print(f'With R$ {money:.2f}, you can buy US$ {convert_money:.2f} and you will have R$ {change:.2f} left as change.')
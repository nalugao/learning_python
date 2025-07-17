# Create a program that asks for the number of kilometers driven by a rented car and the number of days it was rented.
# Calculate the total price to pay, knowing that the car costs R$60 per day and R$0.15 per kilometer driven.

km = float(input('How many kilometers did you drive? '))
days = int(input('How many days did you rent the car? '))

km_cost = km*0.15
day_cost = days*60
total = km_cost+day_cost

#or
#total = (km*0.15) + (days*60)

print(f'The total to pay is R$ {total:.2f}')
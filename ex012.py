# Write an algorithm that reads the price of a product and shows its new price with a 5% discount.

price = float(input('What is the price of the product (R$)? '))

discount = price*0.05
new_price = price-discount

print(f'The discount is R$ {discount:.2f} and the new price is R$ {new_price:.2f}.')
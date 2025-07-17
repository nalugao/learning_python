# Write an algorithm that reads an employee's salary and shows their new salary with a 15% increase.

salary = float(input('Tell me your salary? '))

salary_raise = salary*0.15
new_salary = salary+salary_raise

print(f'Your new salary will be R$ {new_salary:.2f}')
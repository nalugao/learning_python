# um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
# deles e escrevendo o nome do escolhido.

"""import random

a1 = input('First student: ')
a2 = input('Second student: ')
a3 = input('Third student: ')
a4 = input('Forth student: ')

print(f'The student that will help the teacher is {random.choice([a1, a2, a3, a4])}')
"""
#or use list

from random import choice

a1 = input('First student: ')
a2 = input('Second student: ')
a3 = input('Third student: ')
a4 = input('Forth student: ')
lista = [a1, a2, a3, a4]
print(f'The student that will help the teacher is {choice(lista)}')
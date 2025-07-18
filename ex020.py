# o professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro
# alunos e mostre a ordem sorteada.

from random import shuffle #embaralha elementos

a1 = input('First student: ')
a2 = input('Second student: ')
a3 = input('Third student: ')
a4 = input('Fourth student: ')
lista = [a1, a2, a3, a4]

print(f'The order to do the speach is: {shuffle(lista)}')
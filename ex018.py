# faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

import math

a = float(input('Write an angle: '))

sin = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))

print(f'The sine of {a} is {sin:.2f}, the cosine is {cos:.2f} and the tangent is {tan:.2f}.')
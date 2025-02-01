#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

cateto = float(input('Digite o comprimento do cateto oposto: '))
cateto2 = float(input('Digite o comprimento do cateto adjacente: '))

'''hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa vai medir {:.2d}'.format(hi))'''

hipotenusa = hypot(cateto, cateto2)

print('O comprimento da hipotenusa é {:.2f}'.format(hipotenusa))

#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc

numero = float(input('Digite um número: '))

print('O número {} tem a parte inteira {}'.format(numero, trunc(numero)))



num  = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))

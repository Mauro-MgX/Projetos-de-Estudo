# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

from time import sleep

print('Olá mais sou eu Bot!')

print('Hoje que mostrar que consigo descobrir se um número é PAR ou IMPAR')

num = int(input('Digite um número: '))

resto = num % 2

print('Estou pensando...')

sleep(3)

if resto == 0:
    print('O número digitado foi PAR!')
else:
    print('O numero digitado foi IMPAR!')    

print('Obrigado por particiar dessa brincadeira!')
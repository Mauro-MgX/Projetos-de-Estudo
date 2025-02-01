#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua taboada.

numero_base = int(input('Digite um número inteiro:'))

print('Taboada do número {}'.format(numero_base))
print('-'* 12)
print('{} x {:2} = {}'.format(numero_base, 1, numero_base * 1))
print('{} x {:2} = {}'.format(numero_base, 2, numero_base * 2))
print('{} x {:2} = {}'.format(numero_base, 3, numero_base * 3))
print('{} x {:2} = {}'.format(numero_base, 4, numero_base * 4))   
print('{} x {:2} = {}'.format(numero_base, 5, numero_base * 5))   
print('{} x {:2} = {}'.format(numero_base, 6, numero_base * 6))
print('{} x {:2} = {}'.format(numero_base, 7, numero_base * 7))
print('{} x {:2} = {}'.format(numero_base, 8, numero_base * 8))
print('{} x {:2} = {}'.format(numero_base, 9, numero_base * 9))
print('{} x {:2} = {}'.format(numero_base, 10, numero_base * 10))
print('-'* 12)
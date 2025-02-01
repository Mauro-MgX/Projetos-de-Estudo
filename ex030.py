# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.

num = int(input('Digite um número: '))

resto = num % 2

if resto == 0:
    print('O número digitado foi PAR!')
else:
    print('O numero digitado foi IMPAR!')    


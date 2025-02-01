#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
lado1 = float(input('Digite o primeira reta: '))
lado2 = float(input('Digite o segunda reta: '))
lado3 = float(input('Digite o terceira reta: '))


if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2 :
    print('As 3 retas podem formar um triangulo')
else:
    print('As 3 retas não podem formar um triangulo')    
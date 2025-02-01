# faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor

numero = int(input('Digite um número:'))

sucessor = numero + 1

antecessor = numero - 1

print('O nome digitado foi {}, o seu sucessor é {} e o seu antecessor é {}'.format(numero, sucessor , antecessor))

print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(numero, (numero-1), (numero+1)))
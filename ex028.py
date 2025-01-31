# Escreva um programa que faça o computador "Pensar" em um número inteiro entre 0 a 5 e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usúario venceu ou pérdeu.

from random import randint


numero_escolido = randint(0, 5)

print('Olá eu sou Bot !')

nome = str(input('Qual o seu nome ?'))

print('Olá {}'.format(nome))

print('Vamos jogar um jogo ! \n Eu Escolhi um número entre 0 a 5, você consegue adivinhar qual foi!')


numero_digitado = int(input('Digite um numero entre 0 e 5! '))

if int(numero_escolido) == int(numero_digitado):
    print('PARABENS!')
    print('O numero escolhido pelo jogo foi {} '.format(numero_escolido))
    print('O numero digitado pelo jogador foi {} '.format(numero_digitado))
else:
    print('UUUU!')
    print('O numero escolhido pelo jogo foi {} '.format(numero_escolido))
    print('O numero digitado pelo jogador foi {} '.format(numero_digitado))
print('Obrigado por jogar!')

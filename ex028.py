# Escreva um programa que faça o computador "Pensar" em um número inteiro entre 0 a 5 e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usúario venceu ou pérdeu.

from random import randint
from time import sleep

numero_escolido = randint(0, 5)
print('-=-'* 20)
print('Olá eu sou Bot !')
print('-=-'* 20)
nome = str(input('Qual o seu nome ?'))

print('Olá {}'.format(nome))

print('Vamos jogar um jogo ! \nEu Escolhi um número entre 0 a 5, você consegue adivinhar qual foi!')

print('-=-'* 20)
numero_digitado = int(input('Digite um numero entre 0 e 5! '))
print('-=-'* 20)

print('PROCESSANDO')
sleep(3)

if int(numero_escolido) == int(numero_digitado):
    print('-=-'* 20)
    print('PARABENS!')
    print('O numero escolhido pelo jogo foi {} '.format(numero_escolido))
    print('O numero digitado pelo jogador foi {} '.format(numero_digitado))
    print('-=-'* 20)
else:
    print('-=-'* 20)
    print('UUUU!')
    print('O numero escolhido pelo jogo foi {} '.format(numero_escolido))
    print('O numero digitado pelo jogador foi {} '.format(numero_digitado))
    print('-=-'* 20)
print('Obrigado por jogar!')
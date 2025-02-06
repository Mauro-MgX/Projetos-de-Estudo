#Crie um programa que faça o computador jogar jokenpô com você.

from time import sleep
from random import randint


cores = {'limpa':'\033[m', 
         'azul':'\033[36m', 
         'amarelo':'\033[33m', 
         'azul_escuro':'\033[34m', 
         'vermelho': '\033[31m' , 
         'verde':'\033[32m' , 
         'roxo':'\033[35m' , 
         'preto':'\033[m', 
         'branco':'\033[7;40m'
         }


print('-='*20)
print('Olá meu nome é {}Bot{}'.format(cores['azul'], cores['limpa']))
print('-='*20)

print('Eu fui atualizado e estou com uma nova funcionalidade!')
print('Jokenpo!')

print('Você sabe as regras do jogo ?')
print('Digite {}1{} para {}Sim{} ?'.format(cores['azul'], cores['limpa'], cores['azul'], cores['limpa']))
print('Digite {}2{} para {}Não{} ?'.format(cores['amarelo'], cores['limpa'], cores['amarelo'], cores['limpa']))
sabe = int(input(': '))

if sabe == 2 :
    print('As regras são:')
    print('{}Pedra{} ganha de {}Tesoura{},\n{}Tesoura{} ganha de {}Papel{},\n{}Papel{} ganha de {}Pedra{}.'.format(cores['azul'], cores['limpa'], cores['amarelo'], cores['limpa'], cores['amarelo'], cores['limpa'], cores['verde'], cores['limpa'], cores['verde'], cores['limpa'], cores['azul'], cores['limpa']))
    print('Se ambos os jogadores escolherem a mesma opção, é empate.')
    sleep(10)

print('Podemos começar ?')
print('Digite {}1{} para {}Sim{} ?'.format(cores['verde'], cores['limpa'], cores['verde'], cores['limpa']))
print('Digite {}2{} para {}Não{} ?'.format(cores['vermelho'], cores['limpa'], cores['vermelho'], cores['limpa']))
começar = int(input(': '))


if começar == 1 :

    jogada_pc = randint(0,2)

    print('-='*20)
    print('Vamos Começar!')
    print('-='*20)

    print('Digite {}1{} para {}Pedra{} ?'.format(cores['azul'], cores['limpa'], cores['azul'], cores['limpa']))
    print('Digite {}2{} para {}Tesoura{} ?'.format(cores['amarelo'], cores['limpa'], cores['amarelo'], cores['limpa']))
    print('Digite {}3{} para {}Papel{} ?'.format(cores['verde'], cores['limpa'], cores['verde'], cores['limpa']))
    jogada_jogador = int(input(': '))

    print('-='*20)
    print('Processando...')
    print('-='*20)

    sleep(3)

    if jogada_jogador == 1 :
        print('Você escolheu {}Pedra{}'.format(cores['azul'], cores['limpa']))
    elif jogada_jogador == 2 :
        print('Você escolheu {}Tesoura{}'.format(cores['amarelo'], cores['limpa']))
    elif jogada_jogador == 3 :
        print('Você escolheu {}Papel{}'.format(cores['verde'], cores['limpa']))

    if jogada_pc == 1 :
        print('O computador escolheu {}Pedra{}'.format(cores['azul'], cores['limpa']))
    elif jogada_pc == 2 :
        print('O computador escolheu {}Tesoura{}'.format(cores['amarelo'], cores['limpa']))
    elif jogada_pc == 3 :
        print('O computador escolheu {}Papel{}'.format(cores['verde'], cores['limpa']))
    

    if (jogada_pc == 1 and jogada_jogador == 1) or (jogada_pc == 2 and jogada_jogador == 2)  or (jogada_pc == 2 and jogada_jogador == 2) :
        print('-='*20)
        print('DEU EMPATE')
        print('-='*20)
    elif (jogada_jogador == 1 and jogada_pc == 2) or (jogada_jogador == 2 and jogada_pc == 3) or (jogada_jogador == 3 and jogada_pc == 1) : 
        print('-='*20)
        print('VOCÊ GANHOU!!')
        print('-='*20)
    elif (jogada_pc == 1 and jogada_jogador == 2) or (jogada_pc == 2 and jogada_jogador == 3) or (jogada_pc == 3 and jogada_jogador == 1) :   
        print('-='*20)
        print('VOCÊ PERDEU!!')
        print('-='*20)

    print('Obrigado por jogar Jokenpo! com o {}Bot{}'.format(cores['azul'], cores['limpa']))                
else:
    print('Para iniciar uma nova partida rode mais uma vez esse programa!!')

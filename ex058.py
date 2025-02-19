#Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. 
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


from random import randint
from time import sleep

numero_escolido = randint(0, 10)
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
print('Adivinhe quem número eu escolhi!')

nome = str(input('Qual o seu nome ?'))

print('Olá {}'.format(nome))

print('Vamos jogar um jogo ! \nEu Escolhi um número entre 0 a 10, você consegue adivinhar qual foi!')


tentativa = 0
acertou = 0
while acertou == 0 :
    numero_digitado = int(input('Digite um numero entre 0 e 10! '))
    tentativa += 1 
    print('-='*20)
    if int(numero_escolido) != int(numero_digitado):
        print('-=-'* 20)
        print('UUUU! você errou!')
        print('-=-'* 20)
        print('Tente novamente!')

        if numero_escolido > numero_digitado :
            print('O número é maior que {}{}{}'.format(cores['azul'], numero_digitado, cores['limpa']))
        elif numero_escolido < numero_digitado :  
            print('O número é menor que o {}{}{}'.format(cores['azul'], numero_digitado, cores['limpa'])) 

    else:
        acertou = 1    

print('-=-'* 20)
print('PARABENS!')
print('-=-'* 20)
print('Você acertou em {}{}{} tentativas!'.format(cores['verde'], tentativa, cores['limpa']))
print('O numero escolhido pelo jogo foi {} '.format(numero_escolido))
print('O numero digitado pelo jogador foi {} '.format(numero_digitado))

print('Obrigado por jogar Adivinhe quem número eu escolhi! com o {}Bot{}'.format(cores['azul'], cores['limpa']))   

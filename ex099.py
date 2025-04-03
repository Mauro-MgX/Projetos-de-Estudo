#Faça um programa que tem uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
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

def apresentacao(msg):
    print('-=' * 30)
    print(f'{msg}')
    print('-=' * 30)
    
    

apresentacao(f'Olá meu nome é {cores['azul']}Bot{cores['limpa']}')
apresentacao('Eu fui atualizado e estou com uma nova funcionalidade!')
apresentacao('{:^60}'.format('Qual é o Maior Número?'))


def maior(*num):
    print('-='* 30)
    print('Analisando os valores passados...')
    sleep(1)
    maior  = 0 
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.5)
        if valor > maior:
            maior = valor
    print(f'Foram informados {cores["azul"]}{len(num)}{cores["limpa"]} valores ao todo.')
    print(f'O maior valor informado foi {cores['azul']}{maior}{cores['limpa']}.')        

n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)
n6 = randint(1, 10)
maior(n1, n2, n3, n4, n5, n6)
n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
maior(n1, n2, n3)
n1 = randint(1, 10)
n2 = randint(1, 10)
maior(n1, n2)
n1 = randint(1, 10)
maior(n1)
maior()

apresentacao(f'Obrigado utilizar Qual é o Maior Número? do {cores['azul']}Bot{cores['limpa']}')

#Faça um programa que tenha uma lista chamada números e duas funções  chamadas sorteia() e somaPar().
#A primeira função vai sortear 6 números e vai colocá-los dentro da lista.
#A segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint
from time import sleep

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
apresentacao('{:^60}'.format('Sorteio de Números'))


def sorteia(lista):
    print('Sorteado 5 valores da lista: ', end='')
    for cont in range (0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.5)   
    print('PRONTO!')


def somaPar(lista):
    soma = 0 
    for cont in lista:
        if cont % 2 == 0:
            soma += cont
    print(f'Somando os valores pares de {lista}, temos {soma}')           


lista = list()
sorteia(lista)
somaPar(lista)

apresentacao(f'Obrigado utilizar Sorteio de Números do {cores['azul']}Bot{cores['limpa']}')

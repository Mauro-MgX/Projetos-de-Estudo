#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
#Guarde esses resultados em um dicionário. 
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from collections import OrderedDict


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

print('-=' * 20)
print(f'Olá meu nome é {cores['azul']}Bot{cores['limpa']}')
print('-=' * 20)
print('Eu fui atualizado e estou com uma nova funcionalidade!')
print('==' * 30)
print('{:^60}'.format('Jogo de dados para 4 pessoas.'))
print('==' * 30)

jogadas = dict()

for c in range(1, 5):
    dado = randint(1, 6)
    print(f'Jogador {c} tirou {dado} no dado.')
    jogadas['Jodagor'+str(c)] = dado
    sleep(1)

jogadas_ordenadas = dict(sorted(jogadas.items(), key=lambda item: item[1], reverse=True))

print('==' * 30)
print('{:^60}'.format('Ranking dos jogadores'))
print('==' * 30)

cont = 1    
for k, v in jogadas_ordenadas.items():
    print(f'{cont}º lugar: {k} com {v}')
    cont += 1
    sleep(1)
        
print(f'\nObrigado utilizar Jogo de dados para 4 pessoas. do {cores['azul']}Bot{cores['limpa']}')

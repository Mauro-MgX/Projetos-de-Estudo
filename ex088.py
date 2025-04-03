#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. 
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
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

print('-=' * 20)
print(f'Olá meu nome é {cores['azul']}Bot{cores['limpa']}')
print('-=' * 20)
print('Eu fui atualizado e estou com uma nova funcionalidade!')
print('==' * 30)
print('{:^60}'.format('JOGA NA MEGA SENA.'))
print('==' * 30)

total = int(input('Quantos jogos você quer que eu sorteie? '))


jogos = list()
for c in range(0, total):
    jogo = list()
    for l in range(0, 6):
        numero = randint(1, 60)
        while numero in jogo:
            numero = randint(1, 60)
        jogo.append(numero)
        jogo.sort()
    jogos.append(jogo[:])
print(f'-' * 5, f'Sorteando {total} jogos', f'-' * 5)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)

print(f'-' * 5, f'Boa sorte!', f'-' * 5)  
print(f'\nObrigado utilizar JOGA NA MEGA SENA. do {cores['azul']}Bot{cores['limpa']}')

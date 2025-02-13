#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from time import sleep
from datetime import date

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
print('Verificador de maioridade!')

maior = 0
menor = 0
ano_atual = date.today().year

for c in range (0, 7):
    ano = int(input('Digite o seu ano de nascimento: '))
    if ano_atual - ano >= 21:
        maior += 1
    else:
        menor += 1    

print('-='*20)
print('Processando...')
print('-='*20)

sleep(1)
print('Das sete pessoas que você digitou:')
print('{}{} são maiores de idade{}'.format(cores['verde'], maior, cores['limpa']))
print('{}{} são menores de idade{}'.format(cores['vermelho'], menor, cores['limpa']))

print('Obrigado por usar Verificador de maioridade! do {}Bot{}'.format(cores['azul'], cores['limpa']))   
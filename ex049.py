# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
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

print('-='*20)
print('Olá meu nome é {}Bot{}'.format(cores['azul'], cores['limpa']))
print('-='*20)

print('Eu fui atualizado e estou com uma nova funcionalidade!')
print('Tabuada dinamica!')

num = int(input('Digite um número da tabuada que você deseja ver:'))

print('-='*20)
print('Processando...')
print('-='*20)

sleep(2)

for c in range(1, 11) :
    print('{}{}{} x {}{:2}{} = {}{}{}'.format(cores['azul'], num, cores['limpa'], cores['verde'], c, cores['limpa'], cores['roxo'], num * c, cores['limpa']))
    sleep(1)

print('Obrigado por usar a Tabuada dinamica! do {}Bot{}'.format(cores['azul'], cores['limpa']))    

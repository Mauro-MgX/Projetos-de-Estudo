#Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.

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
print('Verificador de qual o maior e o menor peso!')
maior = 0
menor = 0
for c in range (1, 6):
    peso = int(input('Digite o peso da {}ª pessoa (Kg): '.format(c)))
    if c == 1 :
        maior = peso
        menor = peso
    elif peso > maior :    
        maior = peso
    elif peso < menor:
        menor = peso
                
print('-='*20)
print('Processando...')
print('-='*20)

sleep(1)

print('O maior peso digitado foi: {}{}Kg{}'.format(cores['verde'], maior, cores['limpa']))
print('O menor peso digitado foi: {}{}Kg{}'.format(cores['azul'], menor, cores['limpa']))

print('Obrigado por usar Verificador de qual o maior e o menor peso! do {}Bot{}'.format(cores['azul'], cores['limpa']))   
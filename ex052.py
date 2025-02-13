#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
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
print('Verificador de números é primos!')

n = int(input('Digite um número inteiro: '))

print('-='*20)
print('Processando...')
print('-='*20)

sleep(1)

controle = 0
for c in range(1, n +1):
    if n % c == 0 :
        controle += 1 
        print('\033[36m', end='')
    else:
        print('\033[31m', end='')          
    print('{}'.format(c), end=' ')   
    print('\033[m', end='')

if controle == 2:
    print('\nO numero {}{}{} é primo!'.format(cores['azul'], n, cores['limpa']))
else:
    print('\nO número {}{}{} não é primo!'.format(cores['vermelho'], n, cores['limpa']))    

print('\nObrigado por usar Verificador de números é primos! do {}Bot{}'.format(cores['azul'], cores['limpa']))    

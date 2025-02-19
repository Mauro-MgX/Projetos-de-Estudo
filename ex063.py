#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci.
#Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
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
print('Sequencia de fibonacci!')

n = int(input('Digite um número inteiro qualquer: '))

cont = 0

print('-='*20)
print('Processando...')
print('-='*20)

sleep(1)

val1 =  0
val2 = 1
cont = 3
print('{}'.format(val1), end=' -> ')
print('{}'.format(val2), end=' -> ')
while cont <= n:
    val3 = val1 + val2
    print('{}'.format(val3), end=' -> ')
    val1 = val2
    val2 = val3 
    cont += 1    
print('\n Fim da Sequencia de Fibonacci!')

print('Obrigado por usar a Sequencia de fibonacci! do {}Bot{}'.format(cores['azul'], cores['limpa']))    

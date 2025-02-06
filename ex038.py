#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior 
#O se gundo valor é maior 
#Não existe valor maior, os dois são iguais.

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
print('Comparador de Números')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

print('-='*20)
print('Processando...')
print('-='*20)

sleep(3)

if num1 > num2 :
    print('O {}primeiro número{} é {}maior{}'.format(cores['vermelho'], cores['limpa'], cores['azul'], cores['limpa']))
elif num2 > num1 :
    print('O {}segundo número{} é {}maior{}'.format(cores['vermelho'], cores['limpa'], cores['azul'], cores['limpa']))
else:
    print('{}Não existe{} valor maior, os dois são {}iguais{}'.format(cores['vermelho'], cores['limpa'], cores['azul'], cores['limpa']))

print('Obrigado por usar o sistema de convcomparador de números do {}Bot{}'.format(cores['azul'], cores['limpa']))    

#Crie um programa que mostra na tela todos os números pares que estão no intervalo entre 1 e 50.
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
print('Contagem De numeros Pares de 1 a 50!')

for cont in range(2, 51 , 2) :
    print(cont, end=' ')

print('\nObrigado por usar a Contagem De numeros Pares de 1 a 50! do {}Bot{}'.format(cores['azul'], cores['limpa']))    

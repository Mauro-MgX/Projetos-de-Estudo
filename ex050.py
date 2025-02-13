#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidera-o.

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
print('Soma de números pares!')

soma = 0 
cont = 0
for c in range(1 , 7) :
    num = int(input('Digite um número: '))
    if num % 2 == 0 :
        soma += num
        cont += 1
print('-='*20)
print('Processando...')
print('-='*20)

sleep(2)

print('Dos números digitados {}{}{} são pares e a soma de todos os  números pares digitados é: {}{}{}'.format(cores['verde'], cont, cores['limpa'] ,  cores['azul'], soma, cores['limpa']))


print('Obrigado por usar a Soma de números pares! do {}Bot{}'.format(cores['azul'], cores['limpa']))    

#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
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
print('Cadastros de numeros / soma dos mesmos!')
cont = 0
total = 0
num = 0
while num != 999 :

    num = int(input('Digite um número inteiro qualquer (para parar o programa digite 999): '))
    if num != 999 :
        cont += 1
        total += num

print('-='*20)
print('Processando...')
print('-='*20)

sleep(1)


print('O total de números digitados foi: {}{}{}'.format(cores['azul'], cont, cores['limpa']))
print('A soma dos números digitados foi: {}{}{}'.format(cores['azul'], total, cores['limpa']))

print('Obrigado por usar o Cadastros de numeros / soma dos mesmos! do {}Bot{}'.format(cores['azul'], cores['limpa']))    

#Crie um programa que leia vários númeors inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

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
print('Cadastros de numeros / Com media e qual é o maior e qual o menor!')

maior = 0
menor = 0
media = 0
cont  = 0 
continua = 'S'

while continua == 'S' :
    num = int(input('Digite um número inteiro qualquer: '))

    #media 
    media += num
    cont += 1

    #maior e menor
    if cont == 1 :
        maior = menor = num
    else:
        if num > maior :
            maior = num
        if num < menor :
            menor = num     

    continua = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

media = media / cont
print('A media de todos {}{}{} os números digitados foi: {}{:.2f}{}'.format(cores['azul'], cont, cores['limpa'],cores['azul'], media, cores['limpa'] ))
print('O maior número digitado foi: {}{}{}'.format(cores['verde'], maior, cores['limpa']))
print('O menor número digitado foi: {}{}{}'.format(cores['amarelo'], menor, cores['limpa']))


print('Obrigado por usar o Cadastros de numeros / Com media e qual é o maior e qual o menor! do {}Bot{}'.format(cores['azul'], cores['limpa']))    
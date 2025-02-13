#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas .
#No final do programa, mostre:
#A media de idade do grupo
#Qual é o nome do homem mais velho
#Quantas mulheres têm menos de 20 anos.

from time import sleep
#from datetime import date

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
print('Cadastro de multiplas pessoas!')

#ano_atual = date.today().year
medio = 0
nome_maior = ''
idade_maior = 0
mulher_menor = 0
idade_media = 0

for c in range(1, 5):
    print('--------- {}ª PESSOA --------------'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M/F): ')).upper()

    if sexo in 'Ff' and idade < 20:
        mulher_menor += 1

    if c == 1 and sexo in 'Mn' :
        nome_maior = nome  
        idade_maior = idade 
    elif sexo in 'Mn' and idade > idade_maior :
        nome_maior = nome
        idade_maior = idade
    medio += idade 
idade_media = medio / 4

print('-='*20)
print('Processando...')
print('-='*20)

sleep(1)

print('A média de idade do grupo é {}{:.2f}{}'.format(cores['verde'], idade_media, cores['limpa']))

print('O nome do homen mais velho é {}{}{}'.format(cores['azul'], nome_maior, cores['limpa']))

print('O total de mulheres com menos de 20 anos é {}{}{}'.format(cores['roxo'], mulher_menor, cores['limpa']))

print('Obrigado por usar Cadastro de multiplas pessoas! do {}Bot{}'.format(cores['azul'], cores['limpa']))   
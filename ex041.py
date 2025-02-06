#A Confedereção Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SÊNIOR
#Acima: MASTER

from time import sleep
from datetime import date

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
print('Seleção de categoria para a Confederação Nacional de Natação!')

ano = int(input('Digite o seu ano de nascimento: '))

ano_atual = date.today().year

idade = ano_atual - ano

#print(idade)

print('-='*20)
print('Processando...')
print('-='*20)

sleep(3)

if idade <= 9 :
    print('Sua catregoria  é {}MIRIM{}'.format(cores['azul'],cores['limpa']))
elif idade <= 14 :
    print('Sua categoria é {}INFANTIL{}'.format(cores['azul'], cores['limpa']))
elif idade <= 19 :
    print('Sua categoria é {}JUNIOR{}'.format(cores['azul'], cores['limpa']))      
elif idade <= 20 :
    print('Sua categoria é {}SÊNIOR{}'.format(cores['azul'], cores['limpa']))
elif idade > 20 :
    print('Sua categoria é {}MASTER{}'.format(cores['azul'], cores['limpa']))          

print('Obrigado por usar o sistema de Seleção de categoria para a Confederação Nacional de Natação! do {}Bot{}'.format(cores['azul'], cores['limpa']))    
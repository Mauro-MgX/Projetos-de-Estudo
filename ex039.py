# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar.
#Se é a hora de se alistar.
#Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

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
print('Comparador de idade para Alistamento ao Exercito Brasileiro!')

ano_atual = date.today().year

idade_alistamento  = 18

ano = int(input('Digite o seu ano de nascimento: '))
print('Você já serviu ? \nDigite {}1{} para {}Sim{} e Digite {}2{} para {}Não{}.'.format(cores['verde'], cores['limpa'], cores['verde'], cores['limpa'], cores['vermelho'], cores['limpa'], cores['vermelho'], cores['limpa']) )

serviu = int(input(': '))

idade = ano_atual - ano

#print(idade)

print('-='*20)
print('Processando...')
print('-='*20)

sleep(3)

if idade < idade_alistamento and serviu == 2 :
    print('Você ainda vai se alistar ao serviço militar!')
    falta = idade_alistamento - idade
    print('Falta {}{}{} anos para o seu alistamento!'.format(cores['verde'], falta , cores['limpa']))
elif idade > idade_alistamento and serviu == 1:
    print('Você já fez o serviço militar!')
elif idade > idade_alistamento and serviu == 2 :
    print('Já passou do tempo e você não fez o serviço militar!')
    passou = idade - idade_alistamento
    print('Passou {}{}{} anos para do seu prazo alistamento!'.format(cores['vermelho'], passou , cores['limpa']))
elif idade == idade_alistamento and serviu == 1 :
    print('Esse ano você já se alistou no serviço militar!')
elif idade ==  idade_alistamento and serviu == 2 :
    print('Esse ano você precisa se alistar no serviço militar!')
elif idade < idade_alistamento and serviu == 1 :
    print('Você está informando os dados errados!\nNão é possivel se alistar antes dos 18 anos de idade!')    

print('Obrigado por usar o sistema de Comparador de idade para Alistamento ao Exercito Brasileiro! do {}Bot{}'.format(cores['azul'], cores['limpa']))    
#Creie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar.
#No final, mostre:
#A) Qual é o total gasto na compra.
#B) Quantos produtos custam mais de R$1000.
#C) Qual é o nome do produto mais barato.
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
print(f'Olá meu nome é {cores['azul']}Bot{cores['limpa']}')
print('-='*20)

print('Eu fui atualizado e estou com uma nova funcionalidade!')
print('Loja produtos!')

total = prod_1000 = valor_barato = cont = 0
nome_barato = ''
while True :
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: '))
    total += preco
    if preco > 1000 :
        prod_1000 += 1
    if cont == 0 :
        nome_barato = nome
        valor_barato = preco 
    elif preco < valor_barato :
        nome_barato = nome
        valor_barato = preco  
    cont += 1  
    cadastro = ' '           
    while cadastro not in 'SN' :   
        cadastro = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if cadastro == 'N' :
        break
print('-='*20)
print('Processando...')
print('-='*20)

sleep(1)   

print(f'O total da compra foi R${cores['azul']}{total:.2f}{cores['limpa']}')
print(f'Temos {cores['azul']}{prod_1000}{cores['limpa']} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {cores['azul']}{nome_barato}{cores['limpa']} que custa R${cores['azul']}{valor_barato:.2f}{cores['limpa']}')

print(f'Obrigado utilizar a Loja produtos! do {cores['azul']}Bot{cores['limpa']}')    


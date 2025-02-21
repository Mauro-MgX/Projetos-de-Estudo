#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre:
#A Quantas pessoas tem mais de 18 anos.
#B Quantos homens foram cadastrados.
#C Quantas mulheres tem menos de 20 anos.
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
print('Cadastro de pessoas!')
qtd_18 =  qtd_homens = qtd_mulher = cont = 0
cadastro = 'S'
while True :
    idade = ''
    sexo = ''
    print('=='*20)
    if cadastro == 'S' :
        idade = int(input('Digite sua idade: '))
        if idade >= 18 :
            qtd_18 += 1
        while True : 
            sexo = str(input('Digite o sexo [M/F]: ')).upper()
            if sexo in 'Mm' :
                qtd_homens += 1
            elif sexo in 'Ff' and idade < 20: 
                qtd_mulher += 1   
            if sexo in 'MF' :
                break    
    print('=='*20)
    print('=='*20)
    cadastro = ' '
    while cadastro not in 'SN' :
        cadastro = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    print('=='*20)
    if cadastro == 'N':
        break
print('-='*20)
print('Processando...')
print('-='*20)

sleep(1)   

print(f'No total teve {cores['azul']}{qtd_18}{cores['limpa']} pessoas com mais de 18 anos.')
print(f'Ao todo temos {cores['azul']}{qtd_homens}{cores['limpa']} homens cadastrados.')
print(f'E temo {cores['azul']}{qtd_mulher}{cores['limpa']} mulheres com menos de 20 anos')

print(f'Obrigado utilizar o Cadastro de pessoas! do {cores['azul']}Bot{cores['limpa']}')    

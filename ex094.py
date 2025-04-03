#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade do grupo
# C) Uma lista com todas as mulheres
# D) Uma lista com todas as pessoas com idade acima da média

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

print('-=' * 20)
print(f'Olá meu nome é {cores['azul']}Bot{cores['limpa']}')
print('-=' * 20)
print('Eu fui atualizado e estou com uma nova funcionalidade!')
print('==' * 30)
print('{:^60}'.format('Cadastro de Pessoas.'))
print('==' * 30)

pessoas = dict()
pessoa = list()
continuar = ' '
total = 0
idades = 0
while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoas['sexo'] in 'MF':
            break
        else:
            print('ERRO! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    pessoa.append(pessoas.copy())
    total += 1
    idades += pessoas['idade']
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break
print('==' * 30)
#print(pessoa)
print(f'A) O grupo tem {total} pessoas.')
print(f'B) A média de idade é de {idades/total:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in pessoa:
    if p['sexo'] == 'F':
        print(f' {p['nome']}')
print()        
print('D) Lista das pessoas que estão acima da méia: ')
for p in pessoa:
    if p['idade'] >= idades/total:
        print(f'nome = {p['nome']}; sexo = {p['sexo']}; idade = {p['idade']}')
    
print(f'\nObrigado utilizar Cadastro de Pessoas. do {cores['azul']}Bot{cores['limpa']}')

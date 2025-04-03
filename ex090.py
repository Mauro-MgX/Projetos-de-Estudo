#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

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
print('{:^60}'.format('Situação do aluno cadastrado.'))
print('==' * 30)

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))

print(f'Nome é igual a {cores['azul']}{aluno['nome']}{cores['limpa']}')
print(f'Média é igual a {cores['azul']}{aluno['media']}{cores['limpa']}')
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'    
else:
    aluno['situacao'] = 'Reprovado' 

for k, v in aluno.items():
    print(f'{k} é igual a {v}')

print(f'Situação é igual a {cores['azul']}{aluno['situacao']}{cores['limpa']}')       



print(f'\nObrigado utilizar Situação do aluno cadastrado. do {cores['azul']}Bot{cores['limpa']}')


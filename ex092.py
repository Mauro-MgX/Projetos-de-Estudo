#Crie um programa que leia o nomer, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário.
#Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime

ano  = datetime.now().year

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
print('{:^60}'.format('Calculo de Aposentadoria.'))
print('==' * 30)

cadastro = dict()
cadastro['nome'] = str(input('Nome: '))
cadastro['ano_nascimento'] = int(input('Ano de Nascimento: '))
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    idade = ano - cadastro['ano_nascimento']
    cadastro['idade'] = idade
    cadastro['ano_trabalho'] = int(input('Ano de contratação: '))
    data = cadastro['ano_nascimento'] - cadastro['ano_trabalho']
    aposentadoria = 35 - data
    cadastro['aposentadoria'] = aposentadoria
    cadastro['salario'] = float(input('Salário: R$ '))
    print('==' * 30)
    print(cadastro)
    print(f'Nome tem o valor {cadastro['nome']}')
    print(f'Idade tem o valor {cadastro['idade']}')
    print(f'ctps tem o valor {cadastro['ctps']}')
    print(f'contratação tem o valor {cadastro['ano_trabalho']}')
    print(f'salário tem o valor {cadastro['salario']}')
    print(f'aposentadoria tem o valor {cadastro['aposentadoria']}')
else:
    print('==' * 30)
    print(cadastro)
    idade = ano - cadastro['ano_nascimento']
    cadastro['idade'] = idade
    cadastro['ctps'] = 0
    print(f'Nome tem o valor {cadastro['nome']}')
    print(f'Idade tem o valor {cadastro['idade']}')
    print(f'ctps tem o valor {cadastro['ctps']}')

print(f'\nObrigado utilizar Calculo de Aposentadoria. do {cores['azul']}Bot{cores['limpa']}')

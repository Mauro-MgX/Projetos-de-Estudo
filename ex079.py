#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
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
print('{:^60}'.format('Cadastro de números usando Lista V2.'))
print('==' * 30)

lista = []
continua = ' '
while True :
    valor = int(input('Digite um valor: '))
    if valor in lista :
        print('Valor duplicado! Não vou adicionar...') 
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    continua = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if continua == 'N' :
        break     

lista.sort()
print('==' * 30)
print(f'Você digitou os valores {lista}')

print(f'\nObrigado utilizar Cadastro de números usando Lista V2 do {cores['azul']}Bot{cores['limpa']}')    

#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
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
print('{:^60}'.format('Cadastro de números usando Lista.'))
print('==' * 30)

lista = []
for c in range(0, 5) :
    lista.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('==' * 30)
print(f'Você digitou os valores {lista}')
maior  = max(lista)
menor = min(lista)

print(f'O maior valor digitado foi {cores['azul']}{maior}{cores['limpa']} nas posições', end =' ' )
for d, e in enumerate(lista) :
    if maior == e :
        print(f'{d}...', end =' ')

print(f'\nO menor valor digitado foi {cores['azul']}{menor}{cores['limpa']} nas posições', end =' ')
for d, e in enumerate(lista) :
    if menor == e :
        print(f'{d}...', end =' ')

print(f'\nObrigado utilizar Cadastro de números usando Lista do {cores['azul']}Bot{cores['limpa']}')    

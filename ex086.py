#Crie um programa que cria uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.
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
print('{:^60}'.format('Montando uma matriz 3x3.'))
print('==' * 30)

matriz = list()
for c in range(0, 3):
    linha = list()
    for l in range(0, 3):
        linha.append(int(input(f'Digite um valor [{c}, {l}]: ')))
    matriz.append(linha)

print('==' * 30)
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^5}]', end='')
    print()
print('==' * 30)
print(f'\nObrigado utilizar Montando uma matriz 3x3. do {cores['azul']}Bot{cores['limpa']}')


#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
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
print('{:^60}'.format('Montando uma matriz 3x3 aprimorado.'))
print('==' * 30)

matriz = list()
valores_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = 0

for c in range(0, 3):
    linha = list()
    for l in range(0, 3):
        linha.append(int(input(f'Digite um valor [{c}, {l}]: ')))
    matriz.append(linha)

print('==' * 30)
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[{matriz[c][l]:^5}]', end='')
        if matriz[c][l] % 2 == 0:
            valores_pares += matriz[c][l]
        if l == 2:
            soma_terceira_coluna += matriz[c][l]
        if c == 1 and matriz[c][l] > maior_valor_segunda_linha:
            maior_valor_segunda_linha = matriz[c][l]        
    print()
print('==' * 30)

print(f'A soma dos valores pares é {cores['azul']}{valores_pares}{cores['limpa']}')
print(f'A soma dos valores da terceira coluna é {cores['azul']}{soma_terceira_coluna}{cores['limpa']}')
print(f'O maior valor da segunda linha é {cores['azul']}{maior_valor_segunda_linha}{cores['limpa']}')

print(f'\nObrigado utilizar Montando uma matriz 3x3 aprimorado. do {cores['azul']}Bot{cores['limpa']}')


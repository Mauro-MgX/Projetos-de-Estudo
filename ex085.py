#Crie um programa onde o usuário passa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados 
#Os valores pares e impares.
#No final, mostre os valores pares e impares em ordem crescente.


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
print('{:^60}'.format('Analise de pares e ímpares.'))
print('==' * 30)

lista = [[], []]
for c in range(0, 7) :
    numero = int(input(f'Digite o {c+1}º. valor: '))
    if numero % 2 == 0 :
        lista[0].append(numero)
    else:
        lista[1].append(numero)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {cores['azul']}{lista[0]}{cores['limpa']}')
print(f'Os valores ímpares digitados foram: {cores['azul']}{lista[1]}{cores['limpa']}')

print(f'\nObrigado utilizar Analise de pares e ímpares. do {cores['azul']}Bot{cores['limpa']}')    


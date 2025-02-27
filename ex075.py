#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final mostre:
#A) Quantas vezes apareceu o valor 9
#B) Em que posição foi digitado o priemiro valor 3.
#C) Quais foram os números pares.
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
print('{:^30}'.format('Tupla de números'))
print('==' * 30)

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))
num4 = int(input('Digite o último número: '))

numeros = (num1, num2, num3, num4)

print(f'Você digitou os valores {numeros}')
print('==' * 30)
print(f'O valor {cores['azul']}9{cores['limpa']} apareceu {cores['azul']}{numeros.count(9)}{cores['limpa']} vezes.')
print('==' * 30)
if numeros.count(3) == 0 :
    print(f'O valor {cores['azul']}3{cores['limpa']}  não foi digitado em nenhuma posição.')
    print('==' * 30)
else:
    posicao = numeros.index(3)
    posicao += 1
    print(f'O valor {cores['azul']}3{cores['limpa']}  foi digitado na posição {cores['azul']}{posicao}{cores['limpa']}.')
    print('==' * 30)
print('Os valores pares digitados foram' , end=' ')
for cont in numeros :
    if cont % 2 == 0 :
        print(f'{cont}', end=' ')     
print('\n')        
print('==' * 30)

print(f'\nObrigado utilizar a Tupla de números do {cores['azul']}Bot{cores['limpa']}')    

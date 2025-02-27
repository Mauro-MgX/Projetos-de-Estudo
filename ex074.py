#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

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
print('{:^30}'.format('Tupla de números aleatórios'))
print('==' * 30)

num1 = randint(0, 10)
num2 = randint(0, 10)
num3 = randint(0, 10)
num4 = randint(0, 10)
num5 = randint(0, 10)

numero = (num1, num2, num3, num4, num5)
maior  = 0
menor  = 0
print(f'Os valores sorteados foram:', end=' ')
#Sem usar o Max e o Min
#for cont in range(0, len(numero)) :
#    print(numero[cont] , end=' ')
#    if cont == 0 :
#        maior = numero[cont]
#        menor = numero[cont]
#    elif numero[cont] > maior :
#        maior = numero[cont]
#    elif numero[cont] < menor :
#        menor = numero[cont]    
#print(f'\nO maior valor sorteado foi : {maior}')
#print(f'O menor valor sorteado foi : {menor}')

#Usando o Max e Min 
for cont in numero :
    print(cont , end=' ') 
print(f'\nO maior valor sorteado foi : {max(numero)}')
print(f'O menor valor sorteado foi : {min(numero)}')


print(f'Obrigado utilizar a Tupla de números aleatórios do {cores['azul']}Bot{cores['limpa']}')    

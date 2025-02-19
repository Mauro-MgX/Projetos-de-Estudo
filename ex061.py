#Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.

from time import sleep


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

print('-='*20)
print('Olá meu nome é {}Bot{}'.format(cores['azul'], cores['limpa']))
print('-='*20)

print('Eu fui atualizado e estou com uma nova funcionalidade!')
print('10 Primeiros termos de uma PA!')

n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a Razão da PA: '))
#decimo = n + (10 - 1) * r

print('-='*20)
print('Processando...')
print('-='*20)

sleep(1)
#pa = n
#for c in range(n, decimo, r):
#    pa = pa + r
#    print('{}'.format(c), end=' ->')

print('-='*20)
cont = 1
while cont <= 10 :
    print('{}'.format(n), end=' -> ')
    n += r
    cont += 1



print('\nFim da PA!')

print('Obrigado por usar 10 Primeiros termos de uma PA! do {}Bot{}'.format(cores['azul'], cores['limpa']))    

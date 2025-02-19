#Faça um programa que leia um número qualquer e mostre o seu fatorial. 
#Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120


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
print('Fatorial de um número!')

n = int(input('Digite um número: '))
inicio = n
total = n

print('-='*20)
print('Processando...')
print('-='*20)
sleep(1)


print('Calculando o fatorial de {}{}{}!'.format(cores['azul'], n, cores['limpa']))

#Feito usando while
while inicio >= 1 :
    if inicio == n:
        total = inicio
    else: 
        total = total * inicio
    print('{} x '.format(inicio), end='')
    inicio -= 1
print('= {}{}{}'.format(cores['azul'] ,total, cores['limpa']))
inicio = n

# Feito usando for
for c in range(inicio , 0, -1) :
    if c == n:
        total = c
    else: 
        total = total * c
    print('{} x '.format(c), end='')
    c -= 1

print('= {}{}{}'.format(cores['azul'] ,total, cores['limpa']))

print('\nObrigado utilizar o Fatorial de um número! do {}Bot{}'.format(cores['azul'], cores['limpa']))   

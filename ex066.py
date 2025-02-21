#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quanto o usúario digitar o valor 999, que é a condição de parada. 
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando a flag).
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
print(f'Olá meu nome é {cores['azul']}Bot{cores['limpa']}')
print('-='*20)

print('Eu fui atualizado e estou com uma nova funcionalidade!')
print('Cadastros de numeros / e soma de todos!')

num = total = cont =0
while True :
    num = int(input('Digite um número qual quer: [para finalizar digite 999]'))
    if num == 999 :
        break
    total += num
    cont += 1

print('-='*20)
print('Processando...')
print('-='*20)

sleep(1)

print(f'O total de números digitados foram {cores['azul']}{cont}{cores['limpa']}')
print(f'A soma de todos os números digitados é {cores['azul']}{total}{cores['limpa']}')

print(f'Obrigado por usar o Cadastros de numeros / Com media e qual é o maior e qual o menor! do {cores['azul']}Bot{cores['limpa']}') 

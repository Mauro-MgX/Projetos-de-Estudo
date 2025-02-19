#Crie um programa que leia dois valores e mostre um menu na tela:
#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos números
#[5] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

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
print('Bot esta com seu primeio menu!')

print('Para iniciar o menu digite dois numeros!')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
opcao = 0 

while opcao != 5:

    print('-='*20)
    print('Selecione um dos itens abaixo: ')
    print('[1] somar ')
    print('[2] multiplicar ')
    print('[3] maior ')
    print('[4] novos números ')
    print('[5] sair do programa ')
    print('-='*20)
    opcao = int(input('Digite a opção desejada: '))
    print('-='*20)

   

    if opcao == 1:
        print('A soma dos números {}{}{} e {}{}{} é igual {}{}{}'.format(cores['azul'], n1, cores['limpa'], cores['amarelo'], n2, cores['limpa'], cores['verde'], n1 + n2, cores['limpa']) )
    elif opcao == 2:
        print('A multiplicação dos números {}{}{} e {}{}{} é igual {}{}{}'.format(cores['azul'], n1, cores['limpa'], cores['amarelo'], n2, cores['limpa'], cores['verde'], n1 * n2, cores['limpa']))
    elif opcao == 3:
        if n1 > n2:
            print('O número {}{}{} é maior que o número {}{}{}.'.format(cores['azul'], n1, cores['limpa'], cores['amarelo'], n2, cores['limpa']))
        elif n1 < n2:
            print('O número {}{}{} é maior que o número {}{}{}.'.format(cores['amarelo'], n2, cores['limpa'], cores['azul'], n1, cores['limpa']))
        else:
            print('Os números são iguais!')
    elif opcao == 4:
        print('Digite novos números!')
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
       print('Finalizando o programa...')   
    else:
        print('A opção digitada não se encontrada no menu!')   
    sleep(1)    
print('Obrigado utilizar o Primeio menu! com o {}Bot{}'.format(cores['azul'], cores['limpa']))   
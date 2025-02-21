#Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado(número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

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

print('-=' * 20)
print(f'Olá meu nome é {cores['azul']}Bot{cores['limpa']}')
print('-=' * 20)
print('Eu fui atualizado e estou com uma nova funcionalidade!')
print('==' * 30)
print('{:^30}'.format('Caixa Eletrônico para Saques!'))
print('==' * 30)
valor = int(input('Que valor você quer sacar?'))
cedula_50 = cedula_20 = cedula_10 = cedula_1 = 0
sobra = valor 
while True :
    if (sobra - 50) >= 0 :
        sobra -= 50
        cedula_50 += 1
    else:
        if (sobra - 20) >= 0 :
            sobra -= 20
            cedula_20 += 1
        else:
            if (sobra - 10) >= 0 :
                sobra -= 10
                cedula_10 += 1
            else:
                if (sobra - 1) >= 0 :
                    sobra -= 1
                    cedula_1 += 1
                else:
                    break    
                                
print('-='*20)
print('Processando...')
print('-='*20)

sleep(1)   
print('=='*20)
print(f'Total de {cores['azul']}{cedula_50}{cores['limpa']} cédulas de R$50')
print(f'Total de {cores['azul']}{cedula_20}{cores['limpa']} cédulas de R$20')
print(f'Total de {cores['azul']}{cedula_10}{cores['limpa']} cédulas de R$10')
print(f'Total de {cores['azul']}{cedula_1}{cores['limpa']} cédulas de R$1')
print('=='*20)
print('Volte sempre!')

print(f'Obrigado utilizar o Caixa Eletrônico para Saques! do {cores['azul']}Bot{cores['limpa']}')    

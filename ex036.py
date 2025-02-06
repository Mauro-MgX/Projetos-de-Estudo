# Escreva um programa para aprovar o empéstimo bancário para  a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


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
print('Olá me chamo {}Bot{} e vou ajudar você a com seu empréstimo bancario'.format('\033[34m', '\033[m'))
print('-='*20)

salario = float(input('Digite o valor do seu salario em R$: '))
valor_casa = float(input('Digite o valor da casa de deseja comprar em R$: '))
anos = int(input('Digite por quantos anos você pretente pagar essa casa: '))

#print(salario)
#print(valor_casa)
#print(anos)

valor30 = salario * 30 / 100

parcelas = valor_casa / (anos * 12)

#print(valor30)
#print(parcelas)

print('Um momento estou processando...')

sleep(3)

if valor30 >= parcelas :
    print('-='*20)
    print('{}Meus Parabens!{}'.format(cores['verde'], cores['limpa']))
    print('{}O credito foi aprovado!{}'.format(cores['verde'], cores['limpa'])) 
    print('-='*20)
    print('O valor das parcelas para uma casa de R${}{:.2f}{} com uma renda mensal de R${}{:.2f}{} é de R${}{}{}.'.format(cores['vermelho'], valor_casa, cores['limpa'], cores['verde'], salario, cores['limpa'], cores['amarelo'], parcelas, cores['limpa'] ))
else:
    print('-='*20)
    print('{}Sinto muito!{}'.format(cores['vermelho'], cores['limpa']))
    print('{}O credito não foi aprovado!{}'.format(cores['vermelho'], cores['limpa'])) 
    print('-='*20)
    print('O valor da parcela R${}{:.2f}{} é maior que o valor permitido para o seu salario!'.format(cores['vermelho'], parcelas, cores['limpa']))
print('Tenha um bom dia!')



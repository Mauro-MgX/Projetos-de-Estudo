#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#Á vista  Dinhiro/ cheque : 10% de desconto
#Á vista no catão: 5% de desconto 
#Em até 2x no catão: Preço normal
#3x ou mais no cartão: 20% de juros

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
print('Calculo de desconto na forma de pagamento!')


valor = float(input('Digite o valor do produto: '))
print('Selecione a forma de pagamento:')
print('Para forma {}Dinheiro / Cheque{} : digite {}1{}'.format(cores['azul'], cores['limpa'], cores['azul'], cores['limpa']))
print('Para forma {}À vista no cartão{} : digite {}2{}'.format(cores['azul'], cores['limpa'], cores['azul'], cores['limpa']))
print('Para forma {}Parcelado no cartão{} : digite {}3{}'.format(cores['azul'], cores['limpa'], cores['azul'], cores['limpa']))

tipo_pag = int(input(': '))

parcelas = 0


if tipo_pag == 1 :
    print('-='*20)
    print('{:=^40}'.format('Processando...'))
    print('-='*20)

    sleep(3)
    valorf = valor - (valor * 10 / 100)
    print('O valor a ser pago para pagamento a vista no Dinhiro ou Cheque é de R${}{:.2f}{}'.format(cores['azul'], valorf, cores['limpa']))
elif tipo_pag == 2 :
    valorf = valor - (valor * 5 / 100)
    print('-='*20)
    print('{:=^40}'.format('Processando...'))
    print('-='*20)

    sleep(3)
    print('O valor a ser pago para pagamento a vista no Cartão é de R${}{:.2f}{}'.format(cores['azul'], valorf, cores['limpa']))
elif tipo_pag == 3 :
    print('Em quantas vezes você deseja parcelar: ')
    parcelas = int(input(': ')) 
    if parcelas >= 3 :
        valorf = valor + (valor * 20 / 100)
    else:
        valorf = valor
    print('-='*20)
    print('{:=^40}'.format('Processando...'))
    print('-='*20)

    sleep(3)
    print('O valor a ser pago para pagamento en até {}x no Cartão é de R${}{:.2f}{}'.format(parcelas ,cores['azul'], valorf, cores['limpa']))   
else:
    print('{}A opção digitada não existe!{}'.format(cores['vermelho'], cores['limpa']))   

print('Obrigado por usar o sistema de Calculo de desconto na forma de pagamento! do {}Bot{}'.format(cores['azul'], cores['limpa']))            

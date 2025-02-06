#Desenvolva uma lógica que leia o peso e a altura de uma pessoa , calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#Abaixo de 18.5: Abaixo do Peso
#Entre 18.5 e 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade mórbida
#IMC = peso (kg) / (altura (m) x altura (m)). 

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
print('Calculo do IMC!')

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / ( altura ** 2 )


print('-='*20)
print('Processando...')
print('-='*20)

sleep(3)

if imc < 18.5 :
    print('Seu status com base no seu peso e altura é {}Abaixo do Peso{}'.format(cores['azul'], cores['limpa']))
elif imc >= 18.5 and imc < 25 :
    print('Seu status com base no seu peso e altura é {}Peso ideal{}'.format(cores['azul'], cores['limpa']))
elif imc >= 25 and imc < 30 :
    print('Seu status com base no seu peso e altura é {}Sobrepeso{}'.format(cores['azul'], cores['limpa']))
elif imc >= 30 and imc < 40 :
    print('Seu status com base no seu peso e altura é {}Obesidade{}'.format(cores['azul'], cores['limpa']))
elif imc >= 40 :
    print('Seu status com base no seu peso e altura é {}Obesidade mórbida{}'.format(cores['azul'], cores['limpa']))

print('Obrigado por usar o sistema de Calculo do IMC! do {}Bot{}'.format(cores['azul'], cores['limpa']))        
#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
# 1 para binário 
# 2 para octal
# 3 para hexadecimal

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
print('Conversor de Números')

num = int(input('Digite um número decimal qual quer: '))
print('Agora escolha que tipo de converção!')
print('Para converter para {}Binário{} digite {}1{}'.format(cores['vermelho'], cores['limpa'], cores['vermelho'], cores['limpa']))
print('Para converter para {}Octal{} digite {}2{}'.format(cores['roxo'], cores['limpa'], cores['roxo'], cores['limpa']))
print('Para converter para {}Hexadecimal{} digite {}3{}'.format(cores['amarelo'], cores['limpa'], cores['amarelo'], cores['limpa']))
tipo = int(input('Digite o número: '))

print('-='*20)
print('Convertendo o número...')
print('-='*20)

sleep(3)

if tipo == 1 :
    num_convertido = bin(num)
    print('Pronto!!')
    print('O número {}{}{} em Decimal convertido para Binário ficou {}{}{}!'.format(cores['vermelho'], num, cores['limpa'], cores['vermelho'], num_convertido, cores['limpa'] ))
elif tipo == 2:
    num_convertido = oct(num)
    print('Pronto!!')
    print('O número {}{}{} em Decimal convertido para Octal ficou {}{}{}!'.format(cores['roxo'], num, cores['limpa'], cores['roxo'], num_convertido, cores['limpa'] ))
else:        
    num_convertido = hex(num)
    print('Pronto!!')
    print('O número {}{}{} em Decimal convertido para Hexadecimal ficou {}{}{}!'.format(cores['amarelo'], num, cores['limpa'], cores['amarelo'], num_convertido, cores['limpa'] ))

print('Obrigado por usar o sistema de conversão do {}Bot{}'.format(cores['azul'], cores['limpa']))

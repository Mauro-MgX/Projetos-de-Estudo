#Refaça o desafio 035 dos triângulos, acrescentando o recuso de mostrar que tipo de triângulo será formado:
#Equilátereo : Todos os lados iguais
#Isósceles: Dois lados iguais
#Escaleno: todos os lados diferentes

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
print('Analise de Retas para Triângulo!')


lado1 = int(input('Digite a primeira reta: '))
lado2 = int(input('Digite a segunda reta: '))
lado3 = int(input('Digite a terceira reta: '))


print('-='*20)
print('Processando...')
print('-='*20)

sleep(3)


if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2 :
    print('As 3 retas podem formar um triângulo')
    #if lado1 == lado2 and lado2 == lado3 :
    if lado1 == lado2 == lado3 :    
        print('O triângulo que pode ser feito {}Equilátero{}'.format(cores['azul'], cores['limpa']))
    #elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3 :
    elif lado1 != lado2 != lado3 != lado1 :    
        print('O triângulo que pode ser feito {}Escaleno{}'.format(cores['azul'], cores['limpa']))
    else:    
    #elif (lado1 == lado2 and lado2 != lado3) or (lado2 == lado3 and lado3 != lado1) or (lado1 == lado3 and lado3 != lado2) :
        print('O triângulo que pode ser feito {}Isósceles{}'.format(cores['azul'], cores['limpa']))    
else:
    print('As 3 retas não podem formar um triângulo')    

print('Obrigado por usar o sistema de Analise de Retas para Triângulo! do {}Bot{}'.format(cores['azul'], cores['limpa']))        
#Faça um programa que calcule a soma entre todos os números ímpares que são mútiplos de três e que se encontram no intervalo de 1 até 500.
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
print('Soma de todos os números impares que são multiplos de 3 de 1 a 500!')

total = 0
cont = 0
for c in range(1, 500 + 1) :
    if c % 3 == 0 and c % 2 != 0 :
        #print(c, end=' ')
        total += c
        cont += 1
        
print('A soma de todos os {}{}{} valores é  {}{}{}'.format(cores['azul'],cont , cores['limpa'],  cores['verde'],total, cores['limpa']))
print('Obrigado por usar a Soma de todos os números impares que são multiplos de 3 de 1 a 500! do {}Bot{}'.format(cores['azul'], cores['limpa']))    

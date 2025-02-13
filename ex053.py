#Crie um programa que leia uma frase  qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

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
print('Verificador se a frase é um palíndromo!')

frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')
tamanho = len(frase)

print(frase[0:tamanho])

validador = 0
cont_r = tamanho
inverso = ''
for c in range(0, tamanho):
    cont_r = cont_r - 1
    #print('Valor: {} é igual : {}'.format(frase[c], frase[cont_r]))
    inverso += frase[cont_r]
    if frase[c] != frase[cont_r]:
       validador = 1 

print('-='*20)
print('Processando...')
print('-='*20)

sleep(1)

if validador == 1:
    print('A frase digitada {}{}{} e ela ao contrario é {}{}{} não é um palíndromo!'.format(cores['vermelho'], frase, cores['limpa'], cores['vermelho'], inverso, cores['limpa'] ))
else:
    print('A frase digitada {}{}{} e ela ao contrario é {}{}{} essa frase é um palíndromo!'.format(cores['azul'], frase, cores['limpa'], cores['azul'], inverso, cores['limpa'] ))


print('Obrigado por usar Verificador se a frase é um palíndromo! do {}Bot{}'.format(cores['azul'], cores['limpa']))   
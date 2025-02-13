#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
import emoji 

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
print('Contagem regreciva!')

for cont in range(10, -1 , -1) :
    print(cont)
    sleep(1)

print('-='*20)
print(emoji.emojize(':fireworks: :fireworks: :fireworks: Fogos de artificio! :fireworks: :fireworks: :fireworks:'))
print('-='*20)



print('Obrigado por usar a Contagem regreciva! do {}Bot{}'.format(cores['azul'], cores['limpa']))    

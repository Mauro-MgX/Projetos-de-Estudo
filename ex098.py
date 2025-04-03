#Faça um programa que tenha uma função cahama contador(),recaba três parametros: inicio, fim e passo e realize a contagem.
#Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada.

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

def apresentacao(msg):
    print('-=' * 30)
    print(f'{msg}')
    print('-=' * 30)
    
    

apresentacao(f'Olá meu nome é {cores['azul']}Bot{cores['limpa']}')
apresentacao('Eu fui atualizado e estou com uma nova funcionalidade!')
apresentacao('{:^60}'.format('Contagens de Número.'))


#função contador
def contador(inicio, fim, passo):
    if passo < 0:
        passo = passo * -1
    elif passo == 0:
        passo = 1
    
    if inicio > fim:
        passo = passo * -1
        fim = fim - 1
    else:
        passo = passo
        fim = fim + 1
    
    for i in range(inicio, fim, passo):
        print(i, end=' ', flush=True)
        sleep(0.5)
    print('FIM!')    


print('-=' * 30)
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 11, 1)
print('-=' * 30)
print('Contagem de 10 até 0 de 2 em 2')
contador(10, -1, -2)
print('-=' * 30)
print('Agora é sua vez de personalizar a contagem!')

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo:'))

print('-=' * 30)
if passo < 0:
    passo = passo * -1
elif passo == 0:
    passo = 1
print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
contador(inicio, fim, passo)


apresentacao(f'Obrigado utilizar Contagens de Número. do {cores['azul']}Bot{cores['limpa']}')

    
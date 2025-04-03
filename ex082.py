#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores impares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas geradas.
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
print('{:^60}'.format('Cadastro de números usando Lista Pares e Ímpares.'))
print('==' * 30)

lista = []
lista2 = []
lista3 = []
finalisa = ' '
while True :
    numero = int(input('Digite um número: '))
    lista.append(numero)
    finalisa = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if finalisa == 'N' :
        break
print('==' * 30)
for c  in range(len(lista)) :
    if lista[c] % 2 == 0 :
        lista2.append(lista[c])
    else:
        lista3.append(lista[c])    
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista2}')
print(f'A lista de ímpares é {lista3}')
print(f'\nObrigado utilizar Cadastro de números usando Lista Pares e Ímpares. do {cores['azul']}Bot{cores['limpa']}')    

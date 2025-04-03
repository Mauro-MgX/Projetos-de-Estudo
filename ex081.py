#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores ordenada de forma descrescente
#C) Se o valor 5 foi digitado e está ou não na lista.

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
print('{:^60}'.format('Cadastro de números usando Lista V3.'))
print('==' * 30)

continua = ' '
lista = []
while True :

    numero = int(input('Digite um valor: '))
    lista.append(numero)
    continua = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continua == 'N' :
        break
print('==' * 30)
total = len(lista)
print(f'Você digitou {total} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem descrecente são {lista}')
if 5 in lista :
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')    

print(f'\nObrigado utilizar Cadastro de números usando Lista V3 do {cores['azul']}Bot{cores['limpa']}')    

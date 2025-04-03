#Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista.
#No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
#Mais leve a baixo de 70kg e mais pesado acima de 100kg

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
print('{:^60}'.format('Lista de pessoas.'))
print('==' * 30)

finalisa = ' '
pessoa = list()
dado = list()
maior = menor = 0
while True :
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(pessoa) == 0 :
        maior = menor = dado[1]
    else :
        if dado[1] > maior :
            maior = dado[1]
        if dado[1] < menor :
            menor = dado[1]  
    pessoa.append(dado[:])
    dado.clear()
    finalisa = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if finalisa == 'N' :
        break
print('==' * 30)
print(f'Ao todo, você cadastrou {cores['azul']}{len(pessoa)}{cores['limpa']}')

print(f'O maior peso foi de {cores['azul']}{maior:.2f}{cores['limpa']} pessoas. Peso de ', end='')
for p in pessoa :
    if p[1] == maior :
        print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {cores['azul']}{menor:.2f}{cores['limpa']} pessoas. Peso de ', end='')
for p in pessoa :
    if p[1] == menor :
        print(f'[{p[0]}]', end=' ')
print()
print(f'\nObrigado utilizar Lista de pessoas do {cores['azul']}Bot{cores['limpa']}')    

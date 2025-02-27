#Crie um  programa que tenha uma tupla com várias palavras (não usar acentos).
#Depós disso, você deve mostrar, para cada palavra , quais são as suas vogais.
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
print('{:^60}'.format('Quantas vogais tem nas palavras.'))
print('==' * 30)

produtos = ('FEIJAO',  'BANANA',  'CEBOLA',  'LARANJA',  'MANGA',  'ARROZ',  'CARNE', 'FRANGO', 'MARACUJA', 'CAFE')
a = 0
e = 0 
i = 0
o = 0
u = 0
for cont in range(len(produtos)) :
    palavra = produtos[cont]
    print(f'Na palavra {cores['azul']}{palavra}{cores['limpa']} temos ', end=' ')
    for a in range(0, len(palavra)) :
        if palavra[a] in 'AEIOU' :
            print(f'{palavra[a]}' , end=' ')
    print('\n')
print(f'Obrigado utilizar Quantas vogais tem nas palavras do {cores['azul']}Bot{cores['limpa']}')    

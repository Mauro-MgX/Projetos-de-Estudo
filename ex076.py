#Crie um programa que tem uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizado os dados em forma tabular.
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
print('{:^60}'.format('LISTAGEM DE PREÇOS'))
print('==' * 30)

produtos = ('Feijão', 44.22, 
            'Banana', 9.23, 
            'Cebola', 0.40, 
            'Laranja', 15.95, 
            'Manga', 0.61, 
            'Arroz', 34.20, 
            'Carne', 63.45, 
            'Frango', 47.12, 
            'Maracujá', 13.20, 
            'Café', 70)

for cont in range( 0 , len(produtos), 2) :
    print(f'{produtos[cont]:.<50}' + f'R$  {produtos[cont+1]:>7.2f}'  )

print('==' * 30)
print(f'\nObrigado utilizar a Listagem de preços do {cores['azul']}Bot{cores['limpa']}')    

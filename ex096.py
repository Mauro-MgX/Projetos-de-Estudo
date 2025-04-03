#Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular(largura e comprimento) e mostre a área do terreno.
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
print('{:^60}'.format('Controle de Terrenos.'))
print('==' * 30)

def area(l, c):
    a = c * l
    print(f'A área de um terreno {cores['azul']}{l:.1f}{cores['limpa']}x{cores['verde']}{c:.1f}{cores['limpa']} é de {cores['vermelho']}{a:.1f}{cores['limpa']}m².')

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

area(largura, comprimento)

print(f'\nObrigado utilizar Controle de Terrenos. do {cores['azul']}Bot{cores['limpa']}')

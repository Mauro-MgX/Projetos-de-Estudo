# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com taman ho adptável.
# Ex: escreva('Olá, Mundo!')
# Saida:
#-------------------
#    Olá, Mundo!
#-------------------
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
apresentacao('{:^60}'.format('Print usando funções.'))

def escreva(msg):
    tam = len(msg) + 6
    print('=' * tam)
    print(f'   {msg}')
    print('=' * tam)


texto = str(input('Digite um texto: '))
escreva(texto)

apresentacao(f'Obrigado utilizar Print usando funções. do {cores['azul']}Bot{cores['limpa']}')

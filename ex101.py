#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal.
#Indicando se uma pessoa tem voto, NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.



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
apresentacao('{:^60}'.format('Voto'))


def voto(ano=0):
    from datetime import datetime
    ano_server = datetime.now().year
    idade = ano_server - ano
    if idade < 16 :
        return f'Com a idade {idade} NÃO VOTA.'
    elif (idade > 16 and idade < 18) or idade > 65 :
        return f' Com a idade {idade} o voto é OPCIONAL.'
    else: 
        return f'Com a idade {idade} o voto é OBRIGATÓRIO.'


#Programa principal:
ano = int(input('Em que ano você nasceu? '))
print(voto(ano))

    
apresentacao(f'Obrigado utilizar Voto do {cores['azul']}Bot{cores['limpa']}')

    
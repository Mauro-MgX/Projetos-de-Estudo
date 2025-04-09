#Reescreva a Função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
#Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante á função input() do python, só que fazendo a validação.
#Para aceitar apenas um valor numérico.
# Ex: n = leiaInt('Digite um n')

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
apresentacao('{:^60}'.format('Validador V2'))

def leiaInt(mensagem):
    inteiro = ''
    while True:
        try:
            inteiro = int(input(f'{mensagem}'))
        except (ValueError, TypeError):
            print(f'{cores['vermelho']}ERRO! por favor, digite um número inteiro válido.{cores['limpa']}')
        except KeyboardInterrupt:
            print(f'{cores['vermelho']}Usuário! preferiu não informar o número. {cores['limpa']}')
            inteiro = 0
            break
        else:    
            break  
    return inteiro        

def leiaFloat(mensagem):
    real = ''
    while True:
        try:
            real = float(input(f'{mensagem}'))
        except (ValueError, TypeError):
            print(f'{cores['vermelho']}ERRO!  por favor, digite um número real válido.{cores['limpa']}')
        except KeyboardInterrupt:
            print(f'{cores['vermelho']}Usuário! preferiu não informar o número. {cores['limpa']}')
            real = 0
            break
        else:    
            break  
    return real  

# Programa principal
i = leiaInt('Digite um Ininteiro: ')
r = leiaFloat('Digite um Real: ')

print(f'O valor inteiro digitado foi {cores['azul']}{i}{cores['limpa']} e o real foi {cores['azul']}{r}{cores['limpa']}')



apresentacao(f'Obrigado utilizar Validador V2 do {cores['azul']}Bot{cores['limpa']}')

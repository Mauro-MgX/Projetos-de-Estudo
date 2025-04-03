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
apresentacao('{:^60}'.format('Validador'))

def leiaInt(mensagem):
    inteiro = ''
    while True:
        inteiro = str(input(f'{mensagem}'))
        if inteiro.isnumeric():
           break 
        else:
            print(f'{cores['vermelho']}ERRO! Digite um número inteiro válido.{cores['limpa']}')
    return inteiro        

# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {cores['azul']}{n}{cores['limpa']}')



apresentacao(f'Obrigado utilizar Validador do {cores['azul']}Bot{cores['limpa']}')

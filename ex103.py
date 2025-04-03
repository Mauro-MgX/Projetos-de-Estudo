#Faça um program que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
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
apresentacao('{:^60}'.format('Ficha'))

#Funçoes 
def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {cores['azul']}{nome}{cores['limpa']} fez {cores['azul']}{gols}{cores['limpa']} gols no campeonato.')


#Programa Principal
nome = str(input('Nome do jogador: ')).strip()
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome == '':
    ficha(gols=gols)    
else:
    ficha(nome,gols)

apresentacao(f'Obrigado utilizar Ficha do {cores['azul']}Bot{cores['limpa']}')

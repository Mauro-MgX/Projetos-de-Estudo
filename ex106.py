#Faça um mini-sistema que utilize o interactive help do puthon. O usuário vai digitar o comando e o manual vai aparecer.
#Quando o usuário digitar a Palavra 'Fim', O programa se encerrará.
#OBS: Use Cores.
from time import sleep

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

def apresentacao(msg, tam):
    print('-=' * tam)
    print(f'{msg}')
    print('-=' * tam)
    
    
apresentacao(f'Olá meu nome é {cores['azul']}Bot{cores['limpa']}',len('Olá meu nome é Bot')+6)
apresentacao('Eu fui atualizado e estou com uma nova funcionalidade!',len('Eu fui atualizado e estou com uma nova funcionalidade!')+6)
apresentacao('{:^60}'.format('Sistema de Ajuda PyHELP'),len('Sistema de Ajuda PyHELP')+6)

#Funcao
def apresentacaoCores(msg,cor_texto,tam):
    print(f'{cores[cor_texto]}')
    print('-=' * tam)
    print('{:^60}'.format(msg))
    print('-=' * tam)
    print(f'{cores['limpa']}')
    sleep(1)
    


def ajuda(com):
    print(f'{cores['verde']}')
    print(help(com))
    print(f'{cores['limpa']}')
    sleep(1)


#Programa Principal
while True:
    apresentacaoCores('Sistema de Ajuda PyHELP','azul', len('Sistema de Ajuda PyHELP')+6)
    funcao = str(input('Função ou Biblioteca > '))
    if funcao.upper() == 'FIM':
        apresentacaoCores('ATÉ LOGO!','vermelho', len('Sistema de Ajuda PyHELP')+6)
        break
    else:
        ajuda(funcao)
    

apresentacao(f'Obrigado utilizar Sistema de Ajuda PyHELP do {cores['azul']}Bot{cores['limpa']}',len('Obrigado utilizar Sistema de Ajuda PyHELP do Bot')+6)

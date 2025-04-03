#Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
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
print('{:^60}'.format('Aproveitamento do jogador v2.'))
print('==' * 30)

jogador = dict()
gols = list()
total = 0
continuar = ' '
jogadores = list()
while True :
    gols.clear()
    total = 0
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas ele jogou? '))
    for i in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {i}? ')))
        total += gols[i]
    jogador['gols'] = gols[:]
    jogador['total'] = total
    jogadores.append(jogador.copy())
    while True:
        continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if continuar in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if continuar == 'N':
        break
   
print('==' * 30)
print(jogadores)
print('==' * 30)
print(f'{"Cod":<4}{"Nome":<10}{"Gols":<20}{"Total":>15}')
print('--' * 30)
cont = 0
for i in jogadores:
    print(f'{cont:<4}{i['nome']:<10}{str(i['gols']):<20}{i['total']:>15}')
    cont += 1
print('--' * 30)
while True :
    mostra = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if mostra == 999:
        break
    if mostra <= len(jogadores) - 1:    
        print(f'-- Levantamento do jogador {jogadores[mostra]["nome"]}')
        for i, v in enumerate(jogadores[mostra]['gols']):
            print(f'=> No jogo {i}, fez {v} gols.')
    else:    
        print(f'ERRO! Não existe jogador com código {mostra}!')
print(f'\nObrigado utilizar proveitamento do jogador v2. do {cores['azul']}Bot{cores['limpa']}')

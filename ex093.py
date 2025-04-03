#Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
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
print('{:^60}'.format('Aproveitamento do jogador.'))
print('==' * 30)

jogador = dict()
gols = list()
total = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas ele jogou? '))
for i in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
    total += gols[i]
jogador['gols'] = gols[:]
jogador['total'] = total
print('==' * 30)
print(jogador)
print('==' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('==' * 30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(gols):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
    


print(f'\nObrigado utilizar proveitamento do jogador. do {cores['azul']}Bot{cores['limpa']}')

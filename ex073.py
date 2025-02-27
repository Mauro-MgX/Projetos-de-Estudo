#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
#Depois mostre:
#A) Apenas os 5 primeiros colocados
#B) Os últimos 4 colocados da tabela.
#C) Uma lista com os times em ordem alfabética.
#D) Em que posição na tabela está o time da Chapecoense.
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
print('{:^30}'.format('Tabela de times do campeonato brasileiro 2025'))
print('==' * 30)


times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 
         'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 
         'EC Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 
         'Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')
print('==' * 30)
print(f'Lista de times do Basileirão 2025: {times}')
print('==' * 30)
print(f'Os 5 primeiros são: {times[0:5]}')
print('==' * 30)
print(f'Os 4 últimos são: {times[-4:]}')
print('==' * 30)
print(f'Times em ordem alfabética: {sorted(times)}')
print('==' * 30)
print(f'O time da Chapecoense não se encontra nalista dos 20 primeiros times')
print('==' * 30)
print(f'O {cores['azul']}Corinthians{cores['limpa']} está na {cores['azul']}{times.index('Corinthians') + 1}{cores['limpa']}ª posição.')
print('==' * 30)
print(f'Obrigado utilizar a Tabela de times do campeonato brasileiro 2025 do {cores['azul']}Bot{cores['limpa']}')    

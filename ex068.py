#Faça um programa que jogue par ou impar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

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

print('-='*20)
print(f'Olá meu nome é {cores['azul']}Bot{cores['limpa']}')
print('-='*20)

print('Eu fui atualizado e estou com uma nova funcionalidade!')
print('Vamos jogar Par ou Ímpar!')
tipo_result = ''
cont = 0
while True :
    num_pc = randint(0,10)
    num = int(input('Digite um valor: '))
    tipo = ' '
    while tipo not in 'PI' :
        tipo = str(input('Você quer Par ou Ímpar [P/I]')).strip().upper()[0]

    if (num_pc + num) % 2 == 0 :
        tipo_result = 'P'
        print('--'*20)
        print(f'Você jogou {cores['azul']}{num}{cores['limpa']} e o computador {cores['amarelo']}{num_pc}{cores['limpa']}, O total foi {cores['verde']}{num + num_pc}{cores['limpa']} Deu PAR')
        print('--'*20)
    else: 
        tipo_result = 'I'
        print('--'*20)
        print(f'Você jogou {cores['azul']}{num}{cores['limpa']} e o computador {cores['amarelo']}{num_pc}{cores['limpa']}, O total foi {cores['verde']}{num + num_pc}{cores['limpa']} Deu ÍMPAR')
        print('--'*20)
    if tipo == tipo_result :
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
    else:
        print('Você PERDEU!')
        print(f'GAME OVER! Você venceu {cores['azul']}{cont}{cores['limpa']} vezes.')
        break
    print('-='*20)
print(f'Obrigado por jogar Par ou Ímpar! com {cores['azul']}Bot{cores['limpa']}')    

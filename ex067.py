#Faca um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usúario.
#O programa será interrompido quando o número solicitado for negativo.
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
print('Taboadas!')


while True :
    num = int(input('Quer ver a tabuada de qual valor ? '))
    if num < 0 :
        break
    cont = 1
    print('=='*20)
    for c in range(cont , 11 , 1 ) :
        print(f'{cores['azul']}{num}{cores['limpa']} X {cores['azul']}{c:2}{cores['limpa']} = {cores['azul']}{num*c:2}{cores['limpa']}')
    print('=='*20)
print('Taboada foi encerrado.')

print(f'Obrigado por usar Taboadas! do {cores['azul']}Bot{cores['limpa']}') 

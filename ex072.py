#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seui programa deverá ler um número pelo teclado (entre 0 a 20) e mostrá-lo por extenso.
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
print('{:^30}'.format('Contagem de número por extenso'))
print('==' * 30)

numero = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
            'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
            'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze',
            'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
            'Dezenove', 'Vinte')

while True :
    while True :
        num = int(input('Digite um número entre 0 e 20: '))
        if num >= 0 and num <= 20 :
            break
        print('Tente novamente.')

    print(f'O número  digitado foi {cores['azul']}{num}{cores['limpa']} e por extenso ele fica {cores['azul']}{numero[num]}{cores['limpa']}')    

    continua = ' '
    continua = str(input('Deseja continuar [S/N]?')).strip().upper()[0]
    if continua == 'N' :
        break

print(f'Obrigado utilizar a Contagem de número por extenso do {cores['azul']}Bot{cores['limpa']}')    

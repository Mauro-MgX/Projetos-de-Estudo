#Melhore o desafio 061, perguntando para o usúario se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 termos.


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

print('-='*20)
print('Olá meu nome é {}Bot{}'.format(cores['azul'], cores['limpa']))
print('-='*20)

print('Eu fui atualizado e estou com uma nova funcionalidade!')
print('10 Primeiros termos de uma PA!')

n = int(input('Digite o primeiro termo da PA: '))
n_inicio = n 
r = int(input('Digite a Razão da PA: '))
termo  = 10
fim = n + (termo - 1) * r

print('-='*20)
print('Processando...')
print('-='*20)

sleep(1)
pa = n
#for c in range(n, fim, r):
#    pa = pa + r
#    print('{}'.format(c), end=' ->')

print('-='*20)
while n < fim:
    print('{}'.format(n), end=' -> ')
    n += r
    if n == fim :
        print('Quantos termos a mais deseja mostrar ?')
        novo_termo = int(input('Digite a quantidade de termos a mais caso queira parar é so digitar [0]: '))
        termo += novo_termo
        fim = n_inicio + (termo - 1) * r
        print('-='*20)
        print('Processando...')
        print('-='*20)
        sleep(1)

print('\nFim da PA!')


print('Obrigado por usar 10 Primeiros termos de uma PA! do {}Bot{}'.format(cores['azul'], cores['limpa']))    

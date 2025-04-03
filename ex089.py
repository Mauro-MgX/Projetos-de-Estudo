#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

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
print('{:^60}'.format('Nostas dos alunos.'))
print('==' * 30)


lista = list()
aluno = list()
continuar = ' '
while True :
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    aluno.append(media)
    lista.append(aluno[:])
    aluno.clear()
    continuar = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break

print(lista)
print('==' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('--' * 15)
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[3]:>8.1f}')
print('--' * 15)

while True:
    print('==' * 30)
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if mostrar == 999:
        break
    if mostrar <= len(lista) - 1:
        print(f'Notas de {lista[mostrar][0]} são {lista[mostrar][1:3]}')
    else:
        print('Aluno não encontrado!')
print('==' * 30)

print(f'\nObrigado utilizar Nostas dos alunos. do {cores['azul']}Bot{cores['limpa']}')


#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort())
#No final, mostre a lista ordenada na tela.
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
print('{:^60}'.format('Cadastro de números ordenado usando Lista V2.'))
print('==' * 30)

lista = []
for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    if c == 0  or numero > lista[-1]:
      lista.append(numero)
      print('Adicionado ao final da lista...')
    else:    
      pos = 0
      while pos < len(lista):
        if numero <= lista[pos]:
          lista.insert(pos,numero)
          print(f'Adicionado na posição {cores['azul']}{pos}{cores['limpa']} da lista...')
          break
        pos += 1

print('==' * 30)
print(f'Os valores digitados em ordem foram {lista}')

print(f'\nObrigado utilizar Cadastro de números ordenado usando Lista V2 do {cores['azul']}Bot{cores['limpa']}')    

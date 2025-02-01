#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Exemplo: Ana Maria de Souza
#Primeiro Nome  = Ana
#ultimo nome  = Souza

nome = str(input('Digite seu nome completo: ')).strip()
nomeV = nome.split()
total = len(nomeV) - 1

print('Primeiro nome {}'.format(nomeV[0]))

print('Segundo nome {}'.format(nomeV[total]))
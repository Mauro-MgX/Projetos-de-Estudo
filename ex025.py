#crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Digite seu nome completp: ')).strip()
print('Seu nome tem Silta? {}'.format('silva' in nome.lower()))

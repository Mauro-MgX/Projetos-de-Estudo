# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minúsculas
# - Quantas letras ao todo (sem considerar espaços)
# - Quantas letras tem o primeiro nome


nome = str(input('Diogite seu nome completo: '))
print(nome.upper())
print(nome.lower())

print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))

primeiro = nome.split()
#print('Seu nome tem {} letras'.format(len(primeiro[0])))

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
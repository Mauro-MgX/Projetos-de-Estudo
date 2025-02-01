#crie um programa que leia nome da sua cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Digite o nome da sua cidade: ')).strip().lower()


tem = cidade.find('santo')


if tem >= 0:
    print('A cidade começa com Santo')
else:
    print('A cidade não começa com Santo')    
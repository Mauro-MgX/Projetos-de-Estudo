valor = input('Digite algo:')

print('O tipo primitivo desse valor é {}'.format(type(valor)))

print('Só tem espaços ? {}'.format(valor.isspace()))

print('É um número ? {}'.format(valor.isnumeric()))

print('É alfabético ? {}'.format(valor.isalnum()))

print('Está em maiúsculas? {}'.format(valor.isupper()))

print('Está em minúsculas? {}'.format(valor.islower()))

print('Esta capitalizada? {}'.format(valor.istitle()))
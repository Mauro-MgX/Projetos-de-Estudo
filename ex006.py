# Crie um algoritmo que leia um número e mostre o seu dobro, tripo e raiz quadrada.
# criar a raiz quadrada de um numero é a mesma coisa que criar o numero elevado a 0.5
# Exemplo: 81 ** (1/2) = 9.0


numero = int(input('Digite um número: '))


d = numero * 2
t = numero * 3
r = numero ** (1/2)

print('O número digitado foi: {}'.format(numero))

print('O seu dobro é: {}'.format(d))

print('O seu triplo é: {}'.format(t))

print('A sua raiz quadrada é: {:.2f}'.format(r))


print('O número digitado foi: {}'.format(numero))

print('O seu dobro é: {}'.format(numero * 2))

print('O seu triplo é: {}'.format(numero * 3))

print('A sua raiz quadrada é: {:.2f}'.format(numero ** (1/2)))

print('A sua raiz quadrada é: {:.2f}'.format(pow(numero, (1/2))))
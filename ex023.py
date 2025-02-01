# faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

num = int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('A unidade tem: {}'.format(u))
print('A dezena tem: {}'.format(d))
print('A centena tem: {}'.format(c))
print('O milhar tem: {}'.format(m))



#print('A unidade tem: {}'.format(num[3]))
#print('A dezena tem: {}'.format(num[2]))
#print('A centena tem: {}'.format(num[1]))
#print('O milhar tem: {}'.format(num[0]))
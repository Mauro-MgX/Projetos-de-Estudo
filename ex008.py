#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

metros = float(input('Digite o valor em metros:'))

quilometros  = metros / 1000

hectometros = metros  / 100

decametros = metros / 10

centimetros = metros * 100

milimetros = metros * 1000

print('O valor em metros foi: {}'.format(metros))

print('O valor de {} metros em quilometros é: {:.3f}'.format(metros, quilometros))

print('O valor de {} metros em hectometros é: {:.2f}'.format(metros, hectometros))

print('O valor de {} metros em decametros é: {:.1f}'.format(metros, decametros))

print('O valor de {} metros em centimetros é: {:.0f}'.format(metros, centimetros))

print('O valor de {} metros em milimetros é: {:.0f}'.format(metros, milimetros))
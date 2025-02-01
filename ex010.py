#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$1,00 = R$3,27

dinheiro = float(input('Digite o quanto você tem na carteira: R$'))

dolar = 3.27

total_compra = dinheiro / dolar

print('Com R${:.2f} você pode comprar US${:.2f} dólares'.format(dinheiro, total_compra))
#Faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Digite o preço do produto: R$'))

desconto = (preco * 5 /100)
desconto = preco - desconto

#Primeira forma de fazer
#desconto = preco - (preco * 5 /100)

#Segunda forma de fazer
#desconto = (preco * 5 /100)
#desconto = preco - desconto


print('O produto que custava {:.2f}, com a promoção de {}% o valor é R${:.2f}'.format(preco, 5,desconto))
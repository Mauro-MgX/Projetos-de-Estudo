#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

altura = float(input('Digite a altura da parede:'))
largura = float(input('Digite a largura da parede:'))

area = altura * largura 
tinta = area / 2

print('Sua parede tem a dimensão de {} x {} e sua área é de {}m²'.format(altura, largura, area))
print('Para pintar essa parede, você precisará de {}L de tinta'.format(tinta))


#print('A  altura da parede é de {}m \n A largura da parede é de {}m \n A área da parede é de {}m² \n A quantidade de tinta necessária para pintar a parede é de {} Litros de tinta'.format(altura, largura, area, tinta))

#Desenvolva um programa que pergunte a distância de uma Viagem em KM.
#Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$,45 para viagens mais longas

distancia = int(input('Digite a distencia da sua viagem ?'))

if distancia <= 200 :
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('O valor total da viagem vai ser de R${:.2f}'.format(valor))


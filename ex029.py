#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapássar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por Km acima do limite

km = int(input('Digite quantos KM seu carro passou na via ?'))

if km > 80 :
    print('Seu carro foi multado!')
    km_max = km - 80
    valor_multa = km_max * 7
    print('A multa foi de {:.2f} !'.format(valor_multa))
else:
    print('Você estava no limite permitido!')    
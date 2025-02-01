#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapássar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por Km acima do limite

from time import sleep

km = int(input('Digite quantos KM seu carro passou na via ?'))

print('Sua velocidade é de {} km'.format(km))

print("Processando!")
sleep(3)

if km > 80 :
    print('Você foi multado!')
    km_max = km - 80
    valor_multa = km_max * 7
    print('Você passou {} km a mais do permitido'.format(km_max))
    print('A multa foi de {:.2f} !'.format(valor_multa))
else:
    print('Você estava no limite permitido!')    
print('Tenha uma boa viagem!')    
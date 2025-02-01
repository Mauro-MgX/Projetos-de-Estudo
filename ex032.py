# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

ano = int(input('Digite um ano qual quer: '))

if ano // 4 == 0 :
    if ano // 100 == 0 :
        print('O ano digitado {} não é Bissexto!'.format(ano))
    else:
      
        print('O ano digitado {} é Bissexto!'.format(ano))  
else:
    if ano // 400 == 0:
        print('O ano digitado {} é Bissexto!'.format(ano))
    else:
        print('O ano digitado {} não é Bissexto!'.format(ano))

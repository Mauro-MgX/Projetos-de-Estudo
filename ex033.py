#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

#qual é o aimor
maior = n1
if maior < n2 :
    maior = n2
if maior < n3 :
    maior = n3 

#qual é o menor
menor = n1
if menor > n2 :
    menor = n2
if menor > n3 :
    menor = n3 
           

print('O numero maior é  {}'.format(maior))
print('O numero menor é  {}'.format(menor))
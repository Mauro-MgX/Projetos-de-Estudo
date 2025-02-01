#Faça um programa que leia três números e mostre qual é o maior e qual é o menor

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

#qual é o aimor sem usar and no if
#maior = n1
#if maior < n2 :
#    maior = n2
#if maior < n3 :
#    maior = n3 
#qual é o menor sem usar and no if
#menor = n1
#if menor > n2 :
#    menor = n2
#if menor > n3 :
#    menor = n3 

#Outra Logica usando and no if  maior
maior = n1
if n2 > n1 and n2 > n3 :
    maior = n2
if n3 > n1 and n3 > n2 :
    maior = n3

#Outra Logica usando and no if para menor   
menor = n1
if n2 < n1 and n3 < n1 :
    menor = n1
if n3 < n1 and n3 < n2 :
    menor = n3        

print('O numero maior é  {}'.format(maior))
print('O numero menor é  {}'.format(menor))
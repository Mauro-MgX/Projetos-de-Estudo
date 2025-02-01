#Faça um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece primeira vez.
#Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().lower()

letra_a = frase.count('a')

print('A letra A aparece {}'.format(letra_a))

print('A primeira posição da letra A é  {}'.format(frase.find('a')+1))

print('A ultima posição da letra A é  {}'.format(frase.rfind('a')+1))

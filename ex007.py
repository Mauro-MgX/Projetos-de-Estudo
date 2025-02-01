#Desenvolva um prodrama que leia as duas notas de um aluno, calcule e mostre a sua média.
# Média = (Nota1 + Nota2) / 2


nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))

media = (nota1 + nota2) / 2

print('Sua primeira nota foi: {:.1f}'.format(nota1))

print('Sua segunda nota foi: {:.1f}'.format(nota2))

print('Sua média foi: {:.2f}'.format(media))
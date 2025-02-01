#Faça um algoritmo que leia o sário de un funcionário e mostre seu novo salário, com 15% de aumento.


salario = float(input('Digite o salário do funcionário: R$'))


#Primeira forma de fazer
#aumento = salario + (salario  * 15 /100)

#Segunda forma de fazer
aumento = (salario * 15 / 100)

salario_aumento = salario + aumento

print('O salário do funcionário com {}% de aumento é R${:.2f}'.format(15, salario_aumento))



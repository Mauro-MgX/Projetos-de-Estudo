# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00 calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%


salario = float(input('Digite seu Salario: '))

if salario <= 1250.00 :
    acrecimo = (salario * 15 /100)
    novo_salario  = salario + acrecimo
else:  
    acrecimo = (salario * 10 /100)
    novo_salario  = salario + acrecimo    
print('Seu novo salario é R${:.2f}'.format(novo_salario))
  
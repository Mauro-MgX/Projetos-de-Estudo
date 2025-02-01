dias  = int(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados ?'))

valor_dia = dias * 60

valor_rodado = km * 0.15

total = valor_dia + valor_rodado


print('O total a pagar é de R${:.2f}'.format(total))




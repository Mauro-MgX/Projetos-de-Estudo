#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passaa está com os parênteses abertos e fechados na ordem correta.

cores = {'limpa':'\033[m', 
         'azul':'\033[36m', 
         'amarelo':'\033[33m', 
         'azul_escuro':'\033[34m', 
         'vermelho': '\033[31m' , 
         'verde':'\033[32m' , 
         'roxo':'\033[35m' , 
         'preto':'\033[m', 
         'branco':'\033[7;40m'
         }

print('-=' * 20)
print(f'Olá meu nome é {cores['azul']}Bot{cores['limpa']}')
print('-=' * 20)
print('Eu fui atualizado e estou com uma nova funcionalidade!')
print('==' * 30)
print('{:^60}'.format('Analise de parênteses em expressão.'))
print('==' * 30)



expressao = str(input('Digite uma exmpressão: '))

print(len(expressao))
lista = []
for c in range(len(expressao)) :
    lista.append(expressao[c])
print('==' * 30)
if lista.count('(') == lista.count(')') :
    print('Sua expressão está válida!')
else: 
    print('Sua expressão não está válida!')
print('==' * 30)

print(f'\nObrigado utilizar Analise de parênteses em expressão do {cores['azul']}Bot{cores['limpa']}')    

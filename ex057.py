#Faça um programa que leia o Sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

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

print('-='*20)
print('Olá meu nome é {}Bot{}'.format(cores['azul'], cores['limpa']))
print('-='*20)

print('Eu fui atualizado e estou com uma nova funcionalidade!')
print('Validador de digitação!')

regra = 0
sexo_texto = ''
while regra == 0:
    sexo = str(input('Digite o sexo da pessoa [M/F]: ')).strip().upper()
    if (sexo == 'M' or sexo == 'F') and sexo != '' :
        regra = 1
        if sexo == 'M' :
            sexo_texto = 'Masculino' 
        else:
            sexo_texto = 'Feminino'   
    else:
        print('O que foi digitado não é valido!')
        print('Digite um [M/F]!')        
print('O sexo digitado foi: {}{}{}'.format(cores['azul'], sexo_texto, cores['limpa']))

print('Obrigado por usar Validador de digitação! do {}Bot{}'.format(cores['azul'], cores['limpa']))   

#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0: Reprovado
#Média entre 5.0 e 6.9: Recuperação
#Média 7.0 ou superior: Aprovado

from time import sleep

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
print('Média de notas!')

nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))

media = (nt1 + nt2) / 2

print('-='*20)
print('Processando...')
print('-='*20)

sleep(3)

print('Sua media foi {:.1f}'.format(media))
if media < 5.0 :
    print('Você foi {}REPROVADO{}!'.format(cores['vermelho'], cores['limpa']))
    print('Sua media não atingiu o valor minimo para a aprovação!')
elif media > 5.0 and media < 6.9 :
    print('Você ficou de {}RECUPERAÇÃO{}!'.format(cores['amarelo'], cores['limpa']))
    print('Sua media não atingiu o valor minimo para a aprovação!')
elif media >= 7.0 :
    print('Você foi {}APROVADO{}!'.format(cores['verde'], cores['limpa']))
    print('Sua media atingiu o valor para a aprovação!')

print('Obrigado por usar o sistema de Média de notas! do {}Bot{}'.format(cores['azul'], cores['limpa']))       

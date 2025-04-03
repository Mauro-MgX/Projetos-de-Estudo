#Adapte o código do desafio 107, Criando uma função adicional chamada moeda() que consiga mostrar os valores como um valor monetário formatado.
from ex108 import moeda
from ex108 import textos
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


textos.apresentacao(f'Olá meu nome é {cores['azul']}Bot{cores['limpa']}',len('Olá meu nome é Bot')+6)
textos.apresentacao('Eu fui atualizado e estou com uma nova funcionalidade!',len('Eu fui atualizado e estou com uma nova funcionalidade!')+6)
textos.apresentacao('{:^60}'.format('Sistema de Modulos V2'),len('Sistema de Ajuda PyHELP')+6)


num  = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(num, 10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(num, 13))}')


textos.apresentacao(f'Obrigado utilizar Sistema de Modulo V2 do {cores['azul']}Bot{cores['limpa']}',len('Obrigado utilizar Sistema de Ajuda PyHELP do Bot')+6)

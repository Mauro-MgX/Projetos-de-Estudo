#Modifique as funções que foram criadas no desafio107 para que elas aceitem um parâmetro a mais,
#informando por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio108.
from ex109 import moeda
from ex109 import textos
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
textos.apresentacao('{:^60}'.format('Sistema de Modulos V3'),len('Sistema de Ajuda PyHELP')+6)


num  = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(num, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(num, 13, True)}')


textos.apresentacao(f'Obrigado utilizar Sistema de Modulo V3 do {cores['azul']}Bot{cores['limpa']}',len('Obrigado utilizar Sistema de Ajuda PyHELP do Bot')+6)

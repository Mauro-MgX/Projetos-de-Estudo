#Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados Moeda e dado.
#Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.

#Adicione ao moódulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), 
#que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.

from ex111.utilidadescev import moeda
from ex111.utilidadescev import textos
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
textos.apresentacao('{:^60}'.format('Sistema de Modulos V5'),len('Sistema de Ajuda PyHELP')+6)


num  = float(input('Digite o preço: R$'))
moeda.resumo(num, 80, 53)


textos.apresentacao(f'Obrigado utilizar Sistema de Modulo V5 do {cores['azul']}Bot{cores['limpa']}',len('Obrigado utilizar Sistema de Ajuda PyHELP do Bot')+6)

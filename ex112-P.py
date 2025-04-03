#Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
# que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.

from ex112.utilidadescev import moeda
from ex112.utilidadescev import textos
from ex112.utilidadescev import dados


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
textos.apresentacao('{:^60}'.format('Sistema de Modulos V6'),len('Sistema de Ajuda PyHELP')+6)


num  = dados.leiaDinheiro('Digite o preço: R$')
moeda.resumo(num, 80, 53)


textos.apresentacao(f'Obrigado utilizar Sistema de Modulo V6 do {cores['azul']}Bot{cores['limpa']}',len('Obrigado utilizar Sistema de Ajuda PyHELP do Bot')+6)

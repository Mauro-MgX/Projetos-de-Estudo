#Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
#O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.

from ex115.modulos import textos
from ex115.modulos import seletor
from ex115.modulos import cadastro
from ex115.modulos import lista
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


textos.apresentacao(f'Olá meu nome é {cores["azul"]}Bot{cores["limpa"]}',len('Olá meu nome é Bot')+6)
textos.apresentacao('Eu fui atualizado e estou com uma nova funcionalidade!',len('Eu fui atualizado e estou com uma nova funcionalidade!')+6)
textos.apresentacao('{:^60}'.format('Cadastro de Pessoas.'),len('Cadastro de Pessoas.')+6)


while True :
    textos.apresentacao('{:^60}'.format('MENU PRINCIPAL'),len('MENU PRINCIPAL')+15)
    textos.menu(f'{cores["amarelo"]}1{cores["limpa"]} - {cores["azul"]}Ver pessoas cadastradas{cores["limpa"]}')
    textos.menu(f'{cores["amarelo"]}2{cores["limpa"]} - {cores["azul"]}Cadastrar nova Pessoa{cores["limpa"]}')
    textos.menu(f'{cores["amarelo"]}3{cores["limpa"]} - {cores["azul"]}Sair do Sistema{cores["limpa"]}')
    textos.faixa(29)

    op = seletor.seletor(f'{cores["verde"]}Sua opção: {cores["limpa"]}')

    if op == 1:
        textos.apresentacao('{:^60}'.format('PESSOAS CADASTRADAS'),len('PESSOAS CADASTRADAS')+15)
        lista.lerArquivo()
        sleep(3)
    elif op == 2 :
        textos.apresentacao('{:^60}'.format('NOVO CADASTRO'),len('NOVO CADASTRO')+15)
        cadastro.cadastro()
    elif op == 3 :
        textos.apresentacao('{:^60}'.format('Saindo do Sistema...'),len('Saindo do Sistema...')+15)
        sleep(3)
        break
    else:
        textos.apresentacao(f'{cores["vermelho"]}ERRO! Digite uma opção válida!{cores["limpa"]}',len('ERRO! Digite uma opção válida!')+6)

       
textos.apresentacao(f'Obrigado utilizar Cadastro de Pessoas. do {cores["azul"]}Bot{cores["limpa"]}',len('Obrigado utilizar Cadastro de Pessoas do Bot')+6)

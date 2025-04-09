#Cri um codigo em Python que teste se o site Pudim está acessivel pelo computador usado.
import urllib
import urllib.request
    
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

def apresentacao(msg):
    print('-=' * 30)
    print(f'{msg}')
    print('-=' * 30)
    
    
apresentacao(f'Olá meu nome é {cores['azul']}Bot{cores['limpa']}')
apresentacao('Eu fui atualizado e estou com uma nova funcionalidade!')
apresentacao('{:^60}'.format('Teste de site.'))


try:
    site = urllib.request.urlopen('http://www.pudim.com')
except urllib.error.URLError:    
    print(f'{cores['vermelho']}O site Pudim não está acessivel no momento.{cores['limpa']}')
else:
    print(f'{cores['verde']}Consegui acessar o site Pudim com sucesso!{cores['limpa']}')    


apresentacao(f'Obrigado utilizar Teste de site. do {cores['azul']}Bot{cores['limpa']}')

#Crie um programa que tenha a função fatorial() que recebe dois parâmetros:
#O primeiro que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela
#o processo de cálculo do fatorial.
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
apresentacao('{:^60}'.format('Fatorial'))

def fatorial(num, show=False):
    """_summary_
    Calculo de Fatorial
    Args:
        num (_type_): Número que sera calculado o fatorial
        show (bool, optional): Variavel que vai mostrar o calculo na tela. O padrão é False.
    Returns:
        _type_: Dependendo do valor da variavel Show pode mostrar so o resultado do fatoria ou todo o calculo do fatorial na tela.
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c  
    
    if show == True:
        retorno = ''
        for c in range(num, 0, -1):
            retorno = retorno + f'{c}'
            if c > 1:
                retorno = retorno + ' x '
            else:
                retorno = retorno + ' = '
        return retorno + str(f)
    else:  
        return f



print(fatorial(5, show=True))
#help(fatorial)
apresentacao(f'Obrigado utilizar Fatorial do {cores['azul']}Bot{cores['limpa']}')

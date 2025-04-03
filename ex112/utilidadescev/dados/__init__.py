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


def leiaDinheiro(msg):
    """Função criada para formatar e validar o valor digitado
    Garantindo que o valor seja um número real.

    Args:
        msg (str): Mensagem que vai sem mostrada na tela para receber o dado.
    Returns:
        float: Retorna o valor já formatado.
    """
    while True:
        dado = str(input(msg)).strip().replace(',','.')
        if dado.isalpha() or dado == '' :
            print(f'{cores['vermelho']}ERRP! {dado} é um preço inválido!{cores['limpa']}')
        else:
            dado = float(dado)
            break    
    return dado
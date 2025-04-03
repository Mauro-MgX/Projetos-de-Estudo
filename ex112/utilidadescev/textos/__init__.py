#Modulo nde Texto
def apresentacao(msg, tam):
    """Função que faz os texos de apresentação dos exercicios.

    Args:
        msg (str): Vai o texto a ser apresentado.
        tam (int): Vai o tamanho do texto normalmente usando o len()
    """
    print('-=' * tam)
    print(f'{msg}')
    print('-=' * tam)
#Modulos

def metade(num, show=False):
    """Mostra metade do número informado

    Args:
        num (float): Valor que vai ser calculado
        show (bool, optional): Variavel que vai mostrar o valor formatado ou não. O padrão é False.
    Returns:
        Float: Retorna a metade do número informado
    """
    if show :
        return moeda(num / 2)
    else:    
        return num / 2


def dobro(num, show=False):
    """Mostra o dobro do número informado

    Args:
        num (float): Valor que vai ser calculado
        show (bool, optional): Variavel que vai mostrar o valor formatado ou não. O padrão é False.
        
    Returns:
        float: Retorna o dobro do número informado
    """
    if show :
        return moeda(num * 2)
    else:    
        return num * 2


def aumentar(num, v, show=False):
    """Mostra o um acrecimo ao número informado

    Args:
        num (float): Valor que vai ser calculado
        v (int): Valor em % que vai ser creditado ao número informado
        show (bool, optional): Variavel que vai mostrar o valor formatado ou não. O padrão é False.
        
    Returns:
        float: Retorna o número já com o acrecimo informado
    """
    
    if show :
        return moeda(num + (num * v/100))
    else:    
        return num + (num * v/100)


def diminuir(num, v, show=False ):
    """Mostra o um descrecimo ao número informado

    Args:
        num (float): Valor que vai ser calculado
        v (int): Valor em % que vai ser debitado ao número informado
        show (bool, optional): Variavel que vai mostrar o valor formatado ou não. O padrão é False.
        
    Returns:
        float: Retorna o número já com o valor debitado
    """
    if show :
        return moeda(num - (num * v/100))
    else:    
        return num - (num * v/100)


def moeda(num):
    """Função que formata valores do tipo float para moeda.

    Args:
        num (float): Valor que vai ser formatado

    Returns:
        str: Retorna o valor formatado no estilo moeda
    """
    return f'R${num:.2f}'.replace('.', ',')
#Modulos

def metade(num):
    """Mostra metade do número informado

    Args:
        num (float): Valor que vai ser calculado

    Returns:
        float: Retorna a metade do número informado
    """
    return num / 2


def dobro(num):
    """Mostra o dobro do número informado

    Args:
        num (float): Valor que vai ser calculado

    Returns:
        float: Retorna o dobro do número informado
    """
    return num * 2


def aumentar(num, v):
    """Mostra o um acrecimo ao número informado

    Args:
        num (float): Valor que vai ser calculado
        v (int): Valor em % que vai ser creditado ao número informado
        
    Returns:
        float: Retorna o número já com o acrecimo informado
    """
    return num + (num * v/100)


def diminuir(num, v ):
    """Mostra o um descrecimo ao número informado

    Args:
        num (float): Valor que vai ser calculado
        v (int): O valor em % que vai ser debitado ao número informado

    Returns:
        float: Retorna o número já com o valor debitado
    """
    return num - (num * v/100)


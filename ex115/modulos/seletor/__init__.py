def seletor(msg):
    """Função que vai ler a opção cadastrada.

    Args:
        msg (str): mensagem que vai aparecer antes do texto digitado.
    Returns:
        int: retorna a opção digitada.
    """
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
    while True :
        try:
            op = int(input(msg))
        except (ValueError, TypeError):
            print(f'{cores['vermelho']} Erro! Digite uma opção válida!{cores['limpa']}')
        else:
            break
    return op    
        
        

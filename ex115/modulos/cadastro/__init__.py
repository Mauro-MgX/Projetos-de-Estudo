cores = {'limpa':'\033[m', 
         'azul':'\033[36m', 
         'amarelo':'\033[33m', 
         'azul_escuro':'\033[34m', 
         'vermelho': '\033[31m', 
         'verde':'\033[32m', 
         'roxo':'\033[35m', 
         'preto':'\033[m', 
         'branco':'\033[7;40m'
         }

def dado(msg, tipo):
    """Função que coleta os dados digitados pelo usuario."""
    if tipo == 'str':
        while True:
            try: 
                nome = str(input(msg))
            except ValueError:
                print(f"{cores['vermelho']}Erro! Por favor, digite um nome válido.{cores['limpa']}")
            else:
                break
        return nome
    elif tipo == 'int':
        while True:
            try:
                idade = int(input(msg))
            except ValueError:
                print(f"{cores['vermelho']}Erro! Por favor, digite uma idade válida.{cores['limpa']}")
            else:
                break
        return idade    

def AddFinalFila(arquivo, conteudo):
    """Appends content to a file."""
    try:
        with open(arquivo, 'a') as file:
            file.write(conteudo)
    except FileNotFoundError:
        with open(arquivo, 'w') as file:
            pass  # Apenas cria o arquivo
        with open(arquivo, 'a') as file:
            file.write(conteudo)

def cadastro():
    """Função que chama a função de cadastro."""
    nome = dado('Nome: ', 'str')
    if not nome:
        print(f"{cores['vermelho']}Erro ao coletar o nome.{cores['limpa']}")
        return

    idade = dado('Idade: ', 'int')
    if not isinstance(idade, int):
        print(f"{cores['vermelho']}Erro ao coletar a idade.{cores['limpa']}")
        return

    linha = f'{nome};{idade}\n'
    AddFinalFila('cadastro.txt', linha)
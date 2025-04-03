#Faça um programa que tenha a função notas{} que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#Quantidade de notas
#A maior nota
#A menor nota
#A média da turma
#A situação(opcional)
#Adicione também as docstrings da função

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
apresentacao('{:^60}'.format('Notas'))

#Função
def notas(*n, sit=False):
    """_summary_
    Essa função le as notas de um aluno e retorna um dicionário com as seguintes informações:
    Quantidade de notas
    A maior nota
    A menor nota
    A média da turma
    A situação(opcional)
    Args:
        n (_type_): Notas do tipo Float
        sit (bool, optional): Caso seja True a situação da media vai ser adicionada ao dicionário. Defaults to False.
    Returns:
        _type_: Retorna un dicionário com as informações solicitadas.
    """
    dis = dict()
    dis['total'] = len(n)
    dis['maior'] = max(n)
    dis['menor'] = min(n)
    dis['media'] = sum(n) / len(n)
    if sit:
        if dis['media'] >= 7:
            dis['situacao'] = 'Boa'
        elif dis['media'] >= 5:
            dis['situacao'] = 'Razoável'
        elif dis['media'] < 5:
            dis['situacao'] = 'Ruim'
    return dis                



#Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)

apresentacao(f'Obrigado utilizar Notas do {cores['azul']}Bot{cores['limpa']}')

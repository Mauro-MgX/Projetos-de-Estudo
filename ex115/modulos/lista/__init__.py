def lerArquivo():
    try:
        with open('cadastro.txt', 'rt') as file:
          for linha in file:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '') 
            print(f'{dado[0]:<30}{dado[1]:>3} anos')  
    except:
        print('Erro ao ler o arquivo!')

lerArquivo()    
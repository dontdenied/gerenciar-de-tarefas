from funcoes import *
from time import sleep
lista_de_tarefas = []
lista_maior = []
while True:
    print('1 - adicionar nova tarefa\n2 - listar tarefas\n3 - marcar tarefas como concluidas\n4 - exibir tarefas pro prioridade ou categoria\n5 - mostrar tarefas completas/incompletas\n6 - sair do programa')
    escolha = input('\n-> ')
    match escolha:
        case '1':
            dicion = {
            'nome' :input('digite o nome do projeto: '),
            'descricao' : input('digite a descrição do projeto: '),
            'prioridade':input('digite a prioridade do projeto: 1/5: '),
            'categoria': input('digite a categoria do projeto: '),
            'concluido': input('tarefa concluída ? s/n')}
            tarefa = Tarefas(nome_projeto = dicion['nome'], descricao_projeto=dicion['categoria'], prioridade_projeto=dicion['prioridade'], categoria_projeto=dicion['categoria'], concluido=dicion['concluido'])
            lista_maior.append(dicion)
        case '2':
            
            for i, valor in enumerate(lista_maior):
                print(f'no {i+1} item: ')
                sleep(1)
                print(dicion['nome'],"-> " , dicion['descricao'],"-> ", dicion['prioridade'],"-> ", dicion['categoria'],"-> ", dicion['concluido'])
                print()
        case '3':
            print('digite o nome da tarefa para marcar como concluído')
            nome_da_tarefa = input('-> ')
            for tarefa in lista_maior:
                if nome_da_tarefa == tarefa:
                    mudar = input('concluido/incompleto')
                    if "concluido" in mudar:
                        mudar = True
                    elif 'incompleto' in mudar:
                        mudar = False
                    elif 'concluído' in mudar:
                        mudar = True
                    else:
                        print('nao encontrado...')
                        continue
                    tarefa['concluido'] = mudar

        case '4':
            escolha = input('ver por prioridade/categoria: ')
            match escolha:
                case 'prioridade':
                    prioridade = input('digite a prioridade')
                    for tarefa in lista_maior:
                        if tarefa['prioridade'] == prioridade:
                            print(tarefa['prioridade'])
                case 'categoria':
                    categoria = input('digite a categoria')
                    for tarefa in lista_maior:
                        if tarefa['categoria'] == categoria:
                            print(tarefa['categoria'])
                case _:
                    print('nao encontrado, tente novamente')
                    continue

        case '5':
            print()
            
            concluido = input('ver tarefas concluídas/incompletas')
            if 'concluídas' in concluido:
                concluido = True
                for tarefa in lista_maior:
                    if tarefa['concluido'] == True:
                        print(tarefa)
            elif 'incompletas' in concluido:
                concluido = False
                for tarefa in lista_maior:
                    if tarefa['concluido'] == False:
                        print(tarefa)
            elif 'concluida' in concluido:
                concluido = True
                for tarefa in lista_maior:
                    if tarefa['concluido'] == True:
                        print(tarefa)
            elif 'incompleto' in concluido:
                concluido = False
                for tarefa in lista_maior:
                    if tarefa['concluido'] == False:
                        print(tarefa)
            elif 'completo' in concluido:
                concluido = True
                for tarefa in lista_maior:
                    if tarefa['concluido'] == True:
                        print(tarefa)
            else:
                print('não encontrado, tente novamente')
                continue
            for tarefa in lista_maior:
                if tarefa['concluido'] == True:
                    print(tarefa)
                elif tarefa['concluido'] == False:
                    print(tarefa)
                
        case '6':
            print('encerrando programa...')
            sleep(3)
            break

        case _:
            print('escolha indisponível')
            continue









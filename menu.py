from funcoes import *

lista_de_tarefas = []
lista_maior = []
while True:
    print('1 - adicionar nova tarefa\n2 - listar tarefas\n3 - marcar tarefas como concluidas\n4 - exibir tarefas pro prioridade ou categoria\n5 - sair do programa')
    escolha = input('\n-> ')
    if '1' in escolha:
        nome_projeto = input('digite o nome do projeto: ')
        descricao_projeto = input('digite a descrição do projeto: ')
        prioridade_projeto = input('digite a prioridade do projeto: 1/5: ')
        categoria_projeto = input('digite a categoria do projeto: ')
        concluido = input('tarefa concluída ? s/n')
        tarefa = Tarefas(nome_projeto = nome_projeto, descricao_projeto=descricao_projeto, prioridade_projeto=prioridade_projeto, categoria_projeto=categoria_projeto, concluido=concluido)
        
        lista_de_tarefas.append(tarefa.nome_projeto)
        lista_de_tarefas.append(tarefa.descricao_projeto)
        lista_de_tarefas.append(prioridade_projeto)
        lista_de_tarefas.append(categoria_projeto)
        lista_de_tarefas.append(concluido)
        lista_maior.append(lista_de_tarefas)
    elif '2' in escolha:
        print(lista_maior)
    elif '3' in escolha:
        pass
    elif '4' in escolha:
        pass
    elif '5' in escolha:
        print('encerrando...')
        break












class Tarefas:
    lista = []
    def __init__(self, nome_projeto, descricao_projeto, prioridade_projeto, categoria_projeto, concluido = False) -> None:
        self.nome_projeto = nome_projeto
        self.descricao_projeto = descricao_projeto
        self.prioridade_projeto = prioridade_projeto
        self.categoria_projeto = categoria_projeto
        self.concluido = concluido
    def adicionar_tarefa(self, nome_projeto=None, descricao_projeto = None, prioridade_projeto= None, categoria_projeto=None, concluido = False) -> None:
        nome_projeto = input('digite o nome do projeto: ')
        descricao_projeto = input('digite a descrição do projeto: ')
        prioridade_projeto = input('digite a prioridade do projeto: 1/5: ')
        categoria_projeto = input('digite a categoria do projeto: ')
        concluido = input('tarefa concluída ? s/n')
        if 's' in concluido:
            concluido = True
        elif 'n' in concluido:
            concluido = False
        elif not 'n' or 's' in concluido:
            print('inválido')
            exit(1)
        else:
            print('erro')
            exit(1)
        self.nome_projeto = nome_projeto
        self.descricao_projeto = descricao_projeto
        self.prioridade_projeto = prioridade_projeto
        self.categoria_projeto = categoria_projeto 
        self.concluido = concluido
        
    # lista apenas o último item adicionado nas tarefas
    def listar_tarefa(self):
        
        print(self.nome_projeto)
        print(self.descricao_projeto)
        print(self.prioridade_projeto)
        print(self.categoria_projeto)
        print(self.concluido)

    def concluir_tarefa(self):
        concluir = input('concluir tarefa')





class funcionario:                                              # Criação da classe funcionario
    def __init__(self, nome, salario=0.0):
        self.nome = nome
        self.salario = salario

    def get_nome(self):                                         # Método Get
        return self.nome
    def get_salaro(self):                    
        return self.salario
    
    def set_nome(self, novo_valor):                             # Método Set
        self.nome = novo_valor
    def set_salario(self, novo_valor):
        self.salario = novo_valor

    def mostra_dados(self):
        print('-'*26)
        print('Nome: ', self.nome)
        print('Salario: ', self.salario,'\n')

    def bonificacao(self):
        return (self.salario*9)/100

class gerente(funcionario):
    def __init__(self, nome, salario=0.0, qtd_gerencia=1):      # Criação da classe gerente
        super().__init__(nome, salario)
        self.qtd_gerencia = qtd_gerencia
                                                                
    def get_qtd_gerencia(self):                                 # Método Get
        return self.qtd_gerencia
    
    def set_qtd_gerencia(self, novo_valor):                     # Método Set
        self.qtd_gerencia = novo_valor

    def mostra_dados(self):
        super().mostra_dados()
        print('Quatidade que gerencia: ', self.qtd_gerencia)
class conta:                                                # Superclasse
    def __init__(self, nome, saldo=0.0):
        self.nome = nome
        self.saldo = saldo

    def get_nome(self):                                     # Método Get
        return self.nome
    def get_saldo(self):
        return self.saldo
    
    def set_nome(self, novo_nome):                          # Método Set
        self.nome = novo_nome

    def depositar_saldo(self):             # Método de Depósito
        valor_depositado = float(input('Insira o valor a ser depositado: '))
        self.saldo += valor_depositado

    def saque_saldo(self):             # Método de Saque
        valor_saque = float(input('Insira o valor de saque: '))
        if valor_saque < self.saldo:
            self.saldo -= valor_saque
        else:
            print('Saque inválidado, pouco valor na conta.')

class pessoaFisica(conta):
    def __init__(self, nome, genero, saldo=0.0):
        super().__init__(nome, saldo)
        self.genero = genero

    def get_genero(self):
        return self.genero
    
    def set_genero(self, novo_genero):
        if novo_genero == 'M' or novo_genero == 'F':
            self.genero = novo_genero
        else:
            print('Gênero inválido! Inclua "M" ou "F"')

    def saque_saldo(self):
        super().saque_saldo()
        self.saldo -= 2
        print('Taxa de pessoa fisica aplicada, -2 no saldo')

class pessoaJuridica(conta):
    def __init__(self, nome, modalidade, saldo=0.0):
        super().__init__(nome, saldo)
        self.modalidade = modalidade

    def get_modalidade(self):
        return self.modalidade
    
    def set_modalidade(self, nova_modalidade):
        self.modalidade = nova_modalidade

    def saque_saldo(self):
        super().saque_saldo()
        self.saldo -= 5
        print('Taxa de pessoa juridica aplicada, -5 no saldo')
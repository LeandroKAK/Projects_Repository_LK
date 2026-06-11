from abc import ABC, abstractmethod

class produto(ABC):
    def __init__(self, nome, preco_base):
        self.nome = nome
        self.preco_base = preco_base

    # Método Get
    def get_nome(self):
        return self.nome
    
    def get_preco_base(self):
        return self.preco_base
    
    # Método Set
    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_preco_base(self, novo_preco):
        if novo_preco < 0:
            print('Falha no set. Novo preço inválido!')
        else:
            self.preco_base = novo_preco

    @abstractmethod
    def calcular_preco(self):
        pass

class prod_fisico(produto):
    def __init__(self, nome, preco_base, peso=5):
        super().__init__(nome, preco_base)
        self.peso = peso

    # Método Get
    def get_peso(self):
        return self.peso
    
    # Método Set
    def set_peso(self, novo_peso):
        if novo_peso < 0:
            print('Falha no set. Novo peso inválido!')
        else:
            self.preco_base = novo_peso

    # Método Abstrato
    def calcular_preco(self):
        super().calcular_preco()
        return self.preco_base + (4*self.peso)
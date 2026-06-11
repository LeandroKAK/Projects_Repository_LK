class veiculo:
    def __init__(self,  placa, preco):
        self.placa = placa
        self.preco = preco

    # Métodos Get
    def get_placa(self):
        return self.placa
    
    def get_preco(self):
        return self.preco
    
    # Métodos Set
    def set_placa(self, nova_placa):
        self.placa = nova_placa

    def set_preco(self, novo_preco):
        if novo_preco < 0:
            print('Falha no set. Novo preço inválido!')
        else:
            self.preco = novo_preco

class carro(veiculo):
    def __init__(self, placa, preco, portas=4):
        super().__init__(placa, preco)
        self.portas = portas

    # Método Get
    def get_portas(self):
        return self.portas
    
    # Método Set
    def set_portas(self, nova_qtd_portas):
        if nova_qtd_portas < 0:
            print('Falha no set. Número de portas inválido!')
        else:
            self.preco = nova_qtd_portas

    # Método IPVA
    def calcular_IPVA(self):
        return self.preco*(3/100)
    
class onibus(veiculo):
    def __init__(self, placa, preco, assentos=20):
        super().__init__(placa, preco)
        self.assentos = assentos

    # Método Get
    def get_assentos(self):
        return self.assentos

    # Método Set
    def set_assentos(self, nova_qtd_assentos):
        self.assentos = nova_qtd_assentos

    # Método Mostrar Dados
    def mostrar_dados(self):
        print('-=-=-=-\n'
            'Dados do Ônibus:\n'
            'Placa:', self.placa,'\n'
            'Preço:', self.preco,'\n'
            'Número de assentos:',self.assentos)
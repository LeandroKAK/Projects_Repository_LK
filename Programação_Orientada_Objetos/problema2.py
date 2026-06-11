class livro:
    def __init__(self, titulo, preco, paginas=20):
        self.titulo = titulo
        self.preco = preco
        self.paginas = paginas
    
    # Métodos Get

    def get_titulo(self):
        return self.titulo
    def get_preco(self):
        return self.preco
    def get_paginas(self):
        return self.paginas
        
    # Métodos Set

    def set_titulo(self, novo_valor):
        self.titulo = novo_valor
    def set_preco(self, novo_valor):
        self.preco = novo_valor
    def set_paginas(self, novo_valor):
        self.paginas = novo_valor

    # Método mostrar dados

    def mostrar_dados(self):
        print(f'Título: {self.titulo}\n'
            f'Preço: R${self.preco}\n'
            f'Quantidade de páginas: {self.paginas}')
            
    # Método Main

if __name__ == '__main__':
    livro1 = livro(titulo='Dungeons & Drama', preco=60, paginas=250)
    livro2 = livro(titulo='Vilão', preco=70)

    # Teste Get

    print(f'Nome do livro1: {livro1.get_titulo()}')

    # Teste Set

    novo_valor = float(input(f'Substitua o preço do livro 2: '))

    livro2.set_preco(novo_valor)
    print(f'Novo preço do livro2: R${livro2.get_preco()}')

    # Teste Mostrar dados

    print('Todos os dados do livro1:')
    livro1.mostrar_dados()
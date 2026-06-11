from produto_class import produto, prod_fisico

if __name__ == '__main__':

    # Instanciamento dos objetos da classe prod_fisico

    produto_Fis1 = prod_fisico('Carne', 10)
    produto_Fis2 = prod_fisico('Leite', 4, 2)

    print('\n','='*20,'\n')

    # Testes Produto Físico 1
    print('Nome do produto físico 1:', produto_Fis1.get_nome())
    print('Preço base do produto físico 1:', produto_Fis1.get_preco_base())
    print('Alterando o preço base do produto físico 1 para 5:')
    produto_Fis1.set_preco_base(5)
    print('Preço novo do produto físico 1:', produto_Fis1.get_preco_base())
    print('Alterando o preço do produto físico 1 para -10:')
    produto_Fis1.set_preco_base(-10)
    print('Peso do produto físico 1:', produto_Fis1.get_peso())
    print('Preço total do produto físico 1:', produto_Fis1.calcular_preco())

    print('\n','='*20,'\n')

    # Testes Produto Físico 2
    print('Nome do produto físico 2:', produto_Fis2.get_nome())
    print('Preço base do produto físico 2:', produto_Fis2.get_preco_base())
    print('Alterando o preço base do produto físico 2 para 5:')
    produto_Fis2.set_preco_base(5)
    print('Preço novo do produto físico 2:', produto_Fis2.get_preco_base())
    print('Alterando o preço do produto físico 2 para -10:')
    produto_Fis2.set_preco_base(-10)
    print('Peso do produto físico 2:', produto_Fis2.get_peso())
    print('Preço total do produto físico 1:', produto_Fis2.calcular_preco())
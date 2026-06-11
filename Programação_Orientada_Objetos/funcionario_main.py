from funcionario_classe import funcionario, gerente
if __name__ == '__main__':

    # Definição funcionarios
    func1 = funcionario('Murilo', 2100)
    func2 = funcionario('Damylle', 0.05)
    func3 = funcionario('Mariana')

    # Definição gerentes
    gerente1 = gerente('Leandro', 3000000, 3)
    gerente2 = gerente('Hugh', 15000)

    # Testes funcionário
    print(func1)
    print(func1.get_nome())
    func2.set_nome('Daniel')
    print(func2.get_nome())
    print(func3.get_nome())
    print(func1.bonificacao())
    func1.mostra_dados()

    # Testes gerente
    print(gerente2)
    print(gerente2.get_nome())
    gerente1.set_nome('Kenji')
    print(gerente1.get_nome())
    print(gerente1.bonificacao())
    gerente1.mostra_dados()
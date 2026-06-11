from veiculos_class import veiculo, carro, onibus

if __name__ == '__main__':

    # Instanciamento dos objetos da classe carro

    carro1 = carro('XXX-MMNN', 150000, 2)
    carro2 = carro('MMM-NNXX', 200000)

    print('\n','='*20,'\n')

    # Testes Carro 1
    print('Placa do carro 1:', carro1.get_placa())

    print('Preço do carro 1:', carro1.get_preco())
    print('Alterando o preço do carro 1 para 400.000:')
    carro1.set_preco(400000)
    print('Preço novo do carro 1:', carro1.get_preco())
    print('Alterando o preço do carro 1 para -400.000:')
    carro1.set_preco(-400000)

    print('Número de portas do carro 1:', carro1.get_portas)
    print('Alterando o número de portas do carro 1 para 4:')
    carro1.set_portas(4)
    print('Número de portas do carro 1:', carro1.get_portas())
    print('Alterando o número de portas do carro 1 para -4:')
    carro1.set_portas(-4)

    print('IPVA do carro 1:',carro1.calcular_IPVA())

    print('\n','='*20,'\n')

    # Testes Carro 2

    print('Placa do carro 2:', carro2.get_placa())

    print('Preço do carro 2:', carro2.get_preco())
    print('Alterando o preço do carro 2 para 50.000:')
    carro2.set_preco(50000)
    print('Preço novo do carro 2:', carro2.get_preco())
    print('Alterando o preço do carro 2 para -50.000:')
    carro2.set_preco(-50000)

    print('Número de portas do carro 1:', carro1.get_portas)
    print('Alterando o número de portas do carro 2 para 6:')
    carro2.set_portas(6)
    print('Número de portas do carro 2:', carro2.get_portas())
    print('Alterando o número de portas do carro 2 para -8:')
    carro2.set_portas(-8)

    print('IPVA do carro 2:',carro2.calcular_IPVA())

    # Instanciamento de objetos da classe onibus

    onibus1 = onibus('OLA-VIDA', 1000000, 30)

    print('\n','='*20,'\n')

    # Testes Ônibus 1
    print('Placa do Ônibus 1:', onibus1.get_placa())

    print('Preço do Ônibus 1:', onibus1.get_preco())
    print('Alterando o preço do Ônibus 1 para 8.000.000:')
    onibus1.set_preco(8000000)
    print('Preço novo do Ônibus 1:', onibus1.get_preco())
    print('Alterando o preço do Ônibus 1 para -250.000:')
    onibus1.set_preco(-250000)

    print('Assentos do Ônibus 1:', onibus1.get_assentos())

    onibus1.mostrar_dados() 
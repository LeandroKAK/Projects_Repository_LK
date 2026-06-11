from conta_class import conta, pessoaFisica, pessoaJuridica

if __name__ == '__main__':

    print('='*30) # Separador

    # Cadastro 'contas'
    conta1 = conta('Danilo')
    conta2 = conta('Turqueza', 3000)

    # Teste get da classe 'conta'
    print('Saldo conta 1: ', conta1.get_saldo())
    # Teste set da classe 'conta'
    print('Nome atual conta 2: ', conta2.get_nome())
    conta2.set_nome('Daniel')
    print('Novo nome conta 2: ', conta2.get_nome())

    print('='*30) # Separador

    # Cadastro 'pessoaFisica'
    pessoaF1 = pessoaFisica('Mari', 'F', 20000)
    pessoaF2 = pessoaFisica('Kenji', 'M', 4000)
    pessoaF3 = pessoaFisica('Jonatha', 'M')

    # Teste get da classe 'pessoaFisica'
    print('Gênero pessoa fisica 1: ', pessoaF1.get_genero())
    # Teste set da classe 'pessoaFisica'
    print('Gênero atual pessoa fisica 3: ', pessoaF3.get_genero())
    pessoaF3.set_genero('F')
    print('Gênero atual pessoa fisica 3: ', pessoaF3.get_genero())
    # Teste crítico set da classe 'pessoaFisica'
    pessoaF3.set_genero('Não é homi')

    print('='*30) # Separador

    # Cadastro 'pessoaJuridica'
    pessoaJ1 = pessoaJuridica('Soomers', 'MEI',6300)
    pessoaJ2 = pessoaJuridica('Jurai', 'LTDA')

    # Teste get da classe 'pessoaJuridica'
    print('Modalidade pessoa juridica 1: ', pessoaJ1.get_modalidade())
    # Teste set da classe 'pessoaJuridica'
    print('Modalidade atual pessoa juridica 2: ', pessoaJ2.get_modalidade())
    pessoaJ2.set_modalidade('SLU')
    print('Modalidade atual pessoa juridica 2: ', pessoaJ2.get_modalidade())

    print('='*30) # Separador

    # Teste método de depósito
    print('Saldo atual da pessoa fisica 1: ', pessoaF1.get_saldo())
    pessoaF1.depositar_saldo()
    print('Novo saldo da pessoa fisica 1: ', pessoaF1.get_saldo())

    # Teste método de saque
    print('Saldo atual da pessoa fisica 1: ', pessoaF1.get_saldo())
    pessoaF1.saque_saldo()
    print('Novo saldo da pessoa fisica 1: ', pessoaF1.get_saldo())

    # Testes na taxa de saque
    print('Saldo atual da pessoa juridica 1: ', pessoaJ1.get_saldo())
    pessoaJ1.saque_saldo()
    print('Novo saldo da pessoa juridica 1: ', pessoaJ1.get_saldo())

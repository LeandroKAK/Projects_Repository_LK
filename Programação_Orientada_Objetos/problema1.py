def imc(peso, altura):
    return peso/(altura**2)
    
if __name__ == '__main__':
    peso = float(input('Insira o peso da pessoa 1: '))
    altura = float(input('Insira a altura da pessoa 1: '))

    print('IMC da pessoa 1 é: ',imc(peso, altura))

    peso = float(input('Insira o peso da pessoa 2: '))
    altura = float(input('Insira a altura da pessoa 2: '))

    print('IMC da pessoa 2 é: ',imc(peso, altura))
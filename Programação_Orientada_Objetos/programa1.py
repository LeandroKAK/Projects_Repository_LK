def indice(peso,altura):
    indice = peso/(altura*altura)
    return indice

if __name__ == '__main__':
    peso = float(input('Peso:'))
    altura = float(input('Altura:'))

    print("IMC Calculado:",indice(peso, altura))
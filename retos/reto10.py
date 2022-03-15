# Lee un número por teclado e indica si es divisible entre 2 (resto = 0). Si no lo es, también debemos indicarlo.


valorA = int(input('Introduce numero entero: '))

def esPar(numero):
    if numero % 2 == 0:
        print(f'{numero} es divisible por 2.')
    else:
        print(f'{numero} no es divisible entre 2.')


if __name__ == '__main__':
    esPar(valorA)
    print('Fin de la ejecucion ----------------')

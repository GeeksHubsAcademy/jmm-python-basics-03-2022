# Crea una aplicación llamada CalculadoraInversa, nos pedirá 2 operandos (int) y un signo aritmético (str), según este
# último se realizara la operación correspondiente. Al final mostrara el resultado en un cuadro de dialogo.
#
# Los signos aritméticos disponibles son:
#
# +: suma los dos operandos.
# -: resta los operandos.
# *: multiplica los operandos.
# /: divide los operandos, este debe dar un resultado con decimales (float)
# ^: 1º operando como base y 2º como exponente.
# %: módulo, resto de la división entre operando1 y operando2.

def CalculadoraInversa():
    valorA = int(input('Introduce primer operando : '))
    valorB = int(input('Introduce segundo operando : '))
    operando = input('Introduce signo aritmetico: ')

    calculo = eval(f'{valorA} {operando} {valorB}')

    print('El resultado de la operacion es: ',calculo)

if __name__ == '__main__':
    CalculadoraInversa()
    print('Fin de la ejecucion ----------------')
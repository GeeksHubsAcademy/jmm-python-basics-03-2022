# Escribe un programa que realice lo siguiente: declarar una variable N de tipo int, una variable A de tipo float
# y una variable C de tipo str y asigna a cada una un valor.
#
# A continuación muestra por pantalla:
# El valor de cada variable.
# La suma de N + A
# La diferencia de A - N
# El valor numérico correspondiente al valor que contiene la variable C.

N = 10
A = 10.8
C = 'h'

suma = N + A
diferencia = A - N
asC = ord(C) # str to ascii
charC = chr(asC) # ascii to str


if __name__ == '__main__':
    print(N)
    print(A)
    print(C)
    print(suma)
    print(diferencia)
    print(asC)
    print(charC)


# Realiza un programa que declare cuatro variables enteras A, B, C y D y asígnale un valor a cada una. A continuación
# realiza las instrucciones necesarias para que:
#
# B tome el valor de C
# C tome el valor de A
# A tome el valor de D
# D tome el valor de B

A: int = 1
B: int = 2
C: int = 3
D: int = 4

if __name__ == '__main__':
    B = C
    print(B)
    C = A
    print(C)
    A = D
    print(A)
    D = B
    print(D)
    print('Fin de la ejecucion ----------------')
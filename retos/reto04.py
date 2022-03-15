# Escribe un programa que declare una variable entera N y asígnale un valor. A continuación escribe las instrucciones
# que realicen los siguientes:
#
# Incrementar N en 77.
# Decrementarla en 3.
# Duplicar su valor.
#
#
# Si por ejemplo N = 1 la salida del programa será:
#
# Valor inicial de N = 1
# N + 77 = 78
# N - 3 = 75
# N * 2 = 150

N: int = 1

N += 77
print(N)
N -= 3
print(N)
N *= 2
print(N)

if __name__ == '__main__':
    print('Fin de la ejecucion ----------------')
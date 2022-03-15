# Escribe un programa que realice lo siguiente: declarar dos variables X e Y de tipo int, dos variables N y
# M de tipo float y asigna a cada una un valor.
#
# A continuación muestra por pantalla:
# El valor de cada variable.
# La suma  X + Y
# La diferencia  X – Y
# El producto  X * Y
# El cociente  X / Y
# El resto  X % Y
# La suma  N + M
# La diferencia  N – M
# El producto  N * M
# El cociente  N / M
# El resto  N % M
# La suma X + N
# El cociente Y / M
# El resto Y % M
# El doble de cada variable
# La suma de todas las variables
# El producto de todas las variables

X: int = 2
Y: int = 3
N: float = 1.5
M: float = 9.7

suma = X + Y
diferencia = X - Y
producto = X * Y
cociente = X / Y
resto = X % Y
sumaF = N + M
diferenciaF = N - M
productoF = N * M
cocienteF = N / M
restoF = N % M
sum = X + N
coc = Y / M
rest = Y % M

sumaDoble = 2*X + 2*Y + 2*N + 2*M
sumaTodo = X + Y + N + M
productoTodo = X * Y * N * M

if __name__ == '__main__':
    print(suma)
    print(diferencia)
    print(producto)
    print(cociente)
    print(resto)
    print(sumaF)
    print(diferenciaF)
    print(productoF)
    print(cocienteF)
    print(restoF)
    print(sum)
    print(coc)
    print(rest)

    print(sumaDoble)
    print(sumaTodo)
    print(productoTodo)

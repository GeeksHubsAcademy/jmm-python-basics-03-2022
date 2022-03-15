# Realiza una aplicación que nos pida un número de ventas a introducir, después nos pedirá tantas ventas por teclado
# como número de ventas se hayan indicado. Al final mostrara la suma de todas las ventas. Piensa que es lo que
# se repite y lo que no.

ventas = int(input('Introduce numero de ventas: '))
articulos = []

# Creamos lista con precio de cada producto
i = 1
while i <= ventas:
    precioArt = float(input(f'Introduce el valor del articulo {i}: '))
    articulos.append(precioArt)
    i += 1
print(articulos)

# Sumamos el total de los valores de la lista
total = sum(articulos)
print(f'{total} €')

if __name__ == '__main__':

    print('Fin de la ejecucion ----------------')
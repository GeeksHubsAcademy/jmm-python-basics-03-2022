# Lee un número por teclado que pida el precio de un producto (puede tener decimales) y calcule el precio final con IVA.
# El valor del IVA será una constante que será del 21%

def precioIva():
    valor = float(input('Introduce el precio del producto: '))
    IVA = 21
    precio = valor * (1 + IVA/100)
    print(f'El precio final del producto es: {precio} €')

if __name__ == '__main__':
    precioIva()
    print('Fin de la ejecucion ----------------')
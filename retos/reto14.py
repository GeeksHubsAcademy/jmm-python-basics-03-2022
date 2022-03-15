# Muestra los números del 1 al 100 (ambos incluidos) divisibles entre 2 y 3. Utiliza el bucle que desees.

def numeros():
    i = 1
    while i <= 100:
        if i % 2 == 0 or i % 3 == 0:
            print(i)
        i += 1

if __name__ == '__main__':
    numeros()
    print('Fin de la ejecucion ----------------')
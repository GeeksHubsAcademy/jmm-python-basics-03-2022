# Muestra los números del 1 al 100 (ambos incluidos). Usa ara ello un bucle while.

def numeros():
    print('Numbers from 1 to 100:')
    for n in range(1, 101):
        print(n)

if __name__ == '__main__':
    numeros()
    print('Fin de la ejecucion ----------------')
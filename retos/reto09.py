# Haz una aplicación que calcule el área de un circulo (pi*R2). El valor del radio se pedirá por teclado
# (recuerda pasar de str a float). Usa la constante PI y el método pow.
import math

def areaCirculo():
    pi = math.pi
    radio = input('introduce el valor del radio: ')
    area = pi*pow(int(radio),2)
    print('El resultado del area es ', round(area, 3))

if __name__ == '__main__':
    areaCirculo()
    print('Fin de la ejecucion ----------------')
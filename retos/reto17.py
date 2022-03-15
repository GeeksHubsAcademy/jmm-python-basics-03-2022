# Escribe una aplicación que valide el password, esta está definida con una variable de tipo str que contenga una
# contraseña cualquiera. Después se te pedirá que introduzcas la contraseña, tienes 3 intentos. Si la contraseña
# introducida es correcta ya no la pedirá mas mostrando un mensaje diciendo “Enhorabuena”. Piensa bien en la condición
# de salida (3 intentos y si aciertas sale, aunque le queden intentos).

key = 'hola'
intentos = 0

while intentos < 3:
    password = input('Introduce el password: ')
    if password == key:
        print('Bienvenido a la aplicacion')
        break
    intentos += 1

print('Numero de intentos agotados. Login bloqueado.')

if __name__ == '__main__':

    print('Fin de la ejecucion ----------------')
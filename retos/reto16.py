# Crea una aplicación que nos pida un día de la semana y que nos diga si es un día laboral o no.
# Se recomienda el uso de if.


def laborable():
    semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
    dia = input('Introduce dia de la semana: ').lower()

    if semana.count(dia) >= 1:
        print(f'El {dia.lower()} es un dia laborable')
    else:
        print(f'El {dia.lower()} NO es un dia laborable')


if __name__ == '__main__':
    laborable()
    print('Fin de la ejecucion ----------------')
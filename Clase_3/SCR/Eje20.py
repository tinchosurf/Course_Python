# Escribir un programa que determine si un alumno cumplió con una
# asistencia mínima del 75%, solicitando al usuario que ingrese cantidad total
# de clases y cantidad de faltas.


def verificar_asistencia(total_clases, faltas):
    asistencia = ((total_clases - faltas) / total_clases) * 100
    if asistencia >= 75:
        return True
    return False

total_clases = int(input("Ingrese la cantidad total de clases: "))
faltas = int(input("Ingrese la cantidad de faltas: "))

if verificar_asistencia(total_clases, faltas):
    print("El alumno cumplió con la asistencia mínima del 75%")
else:
    print("El alumno no cumplió con la asistencia mínima del 75%")
    


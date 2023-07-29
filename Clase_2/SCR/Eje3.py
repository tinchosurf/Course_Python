""" Redondear el resultado del ejercicio anterior a 2 decimales. """



dias = float(input("Cantidad de dias: "))
precio = float(input("Precio dia: "))
total = precio*dias
r_total = round(total)
#r_total = round(total,2)  seria con dos digitos decimales
print("precio total", r_total)
# Escribir un programa que le solicite al usuario ingresar una unidad de
# medida de temperatura (“celsius” o “fahrenheit”) y el valor de la temperatura,
# para luego convertirla a la otra unidad de medida. Por ejemplo:
# Ingrese unidad de medida de temperatura: celsius
# Ingrese temperatura: 15
# 15 grados celsius equivalen a XX grados fahrenheit.


class ConversorTemp:
    def __init__(self, grados):
        self._grados = grados
    
    def C_a_Faren (self):
        farengaid = self._grados * (9/5) + 32
        return round(farengaid,2)
    
    def F_a_Celc (self):
        celcius = (self._grados - 32 ) * (5/9)
        return round(celcius,2)



numero_a_convertir = ConversorTemp(15)
print(numero_a_convertir.C_a_Faren())
print(numero_a_convertir.F_a_Celc())




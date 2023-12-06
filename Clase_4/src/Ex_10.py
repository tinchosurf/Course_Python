# Escribe una función llamada celsius_a_fahrenheit que tome una temperatura en grados Celsius como argumento y devuelva su equivalente en grados Fahrenheit.


# Resolucion
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura_celsius = 25
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius} grados Celsius equivalen a {temperatura_fahrenheit:.2f} grados Fahrenheit")
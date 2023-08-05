""" Escribir un programa que redondee el número ingresado al entero más
cercano, sin utilizar la función round().
"""
try:
    number_test = float(input("Enter a number: "))
    
    rounded_number = int(number_test + 0.5) if number_test > 0 else int(number_test - 0.5)
    
    print(f"The rounded number is: {rounded_number}")

except ValueError:
    print("Invalid input. Please enter a valid number.")
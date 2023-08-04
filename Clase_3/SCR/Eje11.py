""" Escribir un programa que determine si el valor ingresado es un número
entero o no. Considerar 4 y 4.0 (por ejemplo) como números enteros"""  


try:
    test_number = input("Enter a number: ")
    number = float(test_number)  # Convert the entered value to a floating-point number
    
    if number.is_integer():
        print(f"{number} is an integer.")
    else:
        print(f"{number} isn't an integer. It is a float number.")
    
except ValueError:
    print(f"The {test_number} is not a valid number.")
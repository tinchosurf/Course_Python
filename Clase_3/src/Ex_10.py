""" Escribir un programa que determine si el valor ingresado es un número o
no. """



try: 
    test_number = input ("Enter anything: ")
    
    print (f"{float(test_number)} is a number")
    
except ValueError:

    print(f"{test_number} is not a number")
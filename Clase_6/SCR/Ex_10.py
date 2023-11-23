# Pide al usuario que ingrese una cadena con espacios en blanco al principio y al final, y luego elimina esos espacios.


# Ask the user to input a string with leading and trailing spaces
string_with_spaces = input("Enter a string with spaces at the beginning and end: ")

# Use the strip() method to remove leading and trailing spaces
string_without_spaces = string_with_spaces.strip()

# Display the resulting string without spaces
print("String without leading and trailing spaces:", string_without_spaces)



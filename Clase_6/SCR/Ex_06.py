# Escribe un programa que solicite al usuario una cadena de texto 
# y reemplace todas las ocurrencias de un carácter específico por otro carácter.
# Estas ocurrencias tambien se deberan solicitar al usuario.


# Prompt the user for the input string
original_string = input("Enter a text string: ")

# Prompt the user for the character to replace
char_to_replace = input("Enter the character you want to replace: ")

# Prompt the user for the replacement character
replacement_char = input("Enter the character to replace it with: ")

# Perform the substitution in the input string
modified_string = original_string.replace(char_to_replace, replacement_char)

# Display the resulting string
print("Modified string:", modified_string)
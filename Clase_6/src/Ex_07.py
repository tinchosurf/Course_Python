# Escribe un programa que solicite al usuario una cadena de texto y una subcadena, 
# y luego determine si la subcadena se encuentra en la cadena principal.

# Prompt the user for a main string
main_string = input("Enter a main string: ")

# Prompt the user for a substring
substring = input("Enter a substring: ")

# Check if the substring is present in the main string
if substring in main_string:
    print(f'The substring "{substring}" is found in the main string.')
else:
    print(f'The substring "{substring}" is not found in the main string.')
    
    
"""    
# Ask the user for a main string
main_string = input("Enter a main string: ")

# Ask the user for a substring
substring = input("Enter a substring: ")

# Use the find() method to search for the substring in the main string
index = main_string.find(substring)

# Check if the substring is found in the main string
if index != -1:
    print(f'The substring "{substring}" is found in the main string at index {index}.')
#else:
    print(f'The substring "{substring}" is not found in the main string.')

"""
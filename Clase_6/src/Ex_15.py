# Solicita al usuario que ingrese una dirección de correo electrónico y luego divide la dirección en nombre de usuario y dominio. 


# Solicitar al usuario que ingrese una dirección de correo electrónico
email = input("Ingresa tu dirección de correo electrónico: ")

# Dividir la dirección en nombre de usuario y dominio
parts = email.split("@")

if len(parts) == 2:
    username, domain = parts
    print("Nombre de usuario:", username)
    print("Dominio:", domain)
else:
    print("La dirección de correo electrónico no es válida.")

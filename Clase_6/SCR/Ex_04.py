# Nos han enviado un archivo llamado nombre_clientes.txt, que consta de
# nombres de clientes separados por ";", ya los hemos guardado en una variable:
nombre_clientes = "jorge gomez;pedro perez;julieta gonzalez;ivana lopez"
# Nos solicitaron que mostremos por pantalla cada uno de esos nombres de la
# siguiente manera: "Jorge Gomez" (nombre y apellido que comiencen con mayuscula)

# Dividir la cadena en nombres individuales usando ";" como separador
nombres = nombre_clientes.split(";")

# Inicializar una lista para almacenar los nombres formateados
nombres_formateados = []

# Iterar a través de los nombres y aplicar formato
for nombre in nombres:
    # Dividir el nombre en nombre y apellido
    partes_nombre = nombre.split()
    
    # Inicializar variables para el nombre y apellido formateados
    nombre_formateado = ""
    
    # Iterar a través de las partes del nombre (puede ser nombre y apellido)
    for parte in partes_nombre:
        nombre_formateado += parte.capitalize() + " "
    
    # Agregar el nombre formateado a la lista
    nombres_formateados.append(nombre_formateado.strip())  # Eliminar espacios en blanco adicionales
    
# Imprimir los nombres formateados
for nombre in nombres_formateados:
    print(nombre)


# Nos han proporcionado un archivo de empleados y nos encomendaron ciertas tareas:
# 1- Debemos mostrar los empleados que comiencen con "A".
# 2- Debemos mostrar los empleados que comiencen con "Z".
# 3- Contar los empleados que comienzan con "B".
# 4- Nos pidieron que añadamos a los siguientes empleados: "Juan Carlos", "Agustina", "Daniela", "Florencia"
# 5- Buscar si en la lista se entruentra "Oswaldo", "Raquel" y "Sandra"

# Esta estructura la veremos mas adelante. Su finalidad es abrir el archivo
# que se llama empleados.txt y guardar en una lista todos los nombres de los empleados.
# Debemos trabajar dentro de esa sentencia with.
with open("empleados.txt", encoding="utf8") as file:
    nombres = file.read().split("\n")
    # print(nombres)


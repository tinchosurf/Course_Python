#  Nos solicitaron encriptar el siguiente mensaje y guardarlo en una variable llamada texto_encriptado.
texto = "Programar es el proceso de crear un conjunto de instrucciones para decirle a una computadora cómo realizar una tarea."
# El modo de encriptamiento sera que el texto comienze desde el primer caracter, termine en el ultimo y vaya salteando de a dos caracteres

# Encriptar el texto
texto_encriptado = texto[::2]

print(texto_encriptado)
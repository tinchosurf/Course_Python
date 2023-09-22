# Imprime el siguiente patrón de asteriscos usando bucles for anidados.
# * 
# * * 
# * * * 
# * * * *
# * * * * *
# s=""

# for i in range(0,5):
#     s=s+"* "
#     print(f"{s}")

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()  # Agrega un salto de línea después de imprimir cada fila de asteriscos
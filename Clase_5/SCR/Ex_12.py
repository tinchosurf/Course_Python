# Escribir un programa que enumere los países de la siguiente lista: # pista: enumerate 🥰


# paises = ['Canada', 'USA', 'Mexico', 'Australia', 'China', 'India', 'Corea']

# for index, _ in enumerate(paises):
#     print(index)


paises = ['Canada', 'USA', 'Mexico', 'Australia', 'China', 'India', 'Corea']

for index, country in enumerate(paises):
    print(f"Index: {index}, Country: {country}")
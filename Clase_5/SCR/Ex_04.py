# Ingresa una palabra y cuenta cuántas vocales tiene utilizando un bucle for.


text = input("Type a text: ")
text = text.lower()
count = 0

for letter in text:
    if letter in "aeiou":
        count += 1

print(f"Number of vowels: {count}")

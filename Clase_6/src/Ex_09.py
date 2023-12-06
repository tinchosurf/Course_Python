# Crea un programa que tome una lista de palabras como entrada y las una en una sola cadena utilizando el método join()


# Ask the user to input words separated by spaces
words = input("Enter words separated by spaces: ")

# Split the input into a list of words
word_list = words.split()

# Use the join() method to join the words into a single string
joined_string = " ".join(word_list)

# Display the joined string
print("Joined string:", joined_string)


""" Escribir un programa que devuelva la nota de un examen en base a la
puntuación obtenida:
0-60: F
61-70: D
71-80: C
81-90: B
91-100: A
"""
try:
    grade = float(input("Enter the grade: "))
    
    if 0 <= grade <= 60:
        print(f"Your grade is F with {grade}")
    elif 61 <= grade <= 70: 
        print(f"Your grade is D with {grade}")
    elif 71 <= grade <= 80: 
        print(f"Your grade is C with {grade}")
    elif 81 <= grade <= 90: 
        print(f"Your grade is B with {grade}")
    elif 91 <= grade <= 100: 
        print(f"Your grade is A with {grade}")
    else:
        print(f"The grade is incorrect. Please enter a number between 0 and 100: {grade}")

except ValueError:
    print(f"{grade} is not a valid number.")


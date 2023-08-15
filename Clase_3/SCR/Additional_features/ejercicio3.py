# Para pagar un determinado impuesto se debe ser mayor de 18 años y tener unos 
# ingresos iguales o superiores a 20000 ARS mensuales. Escribir un programa que pregunte 
# al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que pagar un impuesto o no.


age = int(input("put your age: "))


if age >=18:
    income = float(input("put your income: "))
    print("you are adult")
    if income < 20000:
        print("but don't have to pay, your income is low")
    else:
        print("and your income is high you must pay the tax")
else:
    print("you are minor don't have to pay")
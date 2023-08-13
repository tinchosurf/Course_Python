"""Escribir un programa que calcule el salario a cobrar en base a las horas
trabajadas.
Menos de 10 horas: no se paga nada.
Primeras 40 horas: $1500.
Horas adicionales más allá de las primeras 40: $2000."""

class Person:
    def __init__(self, name, height, age, weight):
        self._name = name
        self._height = height
        self._age = age
        self._weight = weight
    
    def eat(self):
        pass
    
    def walk(self):
        pass
    
    def __str__(self):
        return f"{self._name}: "+ f"\n *Age: {self._age}\n *Height: {self._height}\n *Weight: {self._weight}"

class Worker(Person):
    def __init__(self, name, height, age, weight, hours_worked):
        super().__init__(name, height, age, weight)
        self._hours_worked = hours_worked
        
        if hours_worked < 10:
            self._salary = 0
        elif 10 <= hours_worked <= 40:
            self._salary = 1500 * self._hours_worked
        else:
            self._salary = 1500 * 40 + 2000 * (self._hours_worked - 40)
    
    def __str__(self):
        
        return super().__str__() + f"\n *Salary: ${self._salary}"

trabajador1 = Worker("Martin", 1.83, 40, 101, 40)
trabajador2 = Worker("Erika", 1.63, 32, 65, 50)


print(trabajador1)
print(trabajador2)

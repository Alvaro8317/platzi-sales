class Person:
    def __init__(self,name,age): #Permite inicializar los valores
        self.name = name #Se usa self para tener referencias internas hacia la clase
        self.age = age
    def greet(self):
        print(f"Hello mothefucker! My name is {self.name} and my age is {self.age}")
if __name__ == '__main__':
    Alvaro = Person('Alvaro', 24)
    print(f"Age: {Alvaro.age}")
    Alvaro.greet()
"""
passwordin = '12345'

def password_required(func):
    def wrapper(): #La función interna suele llamarse wrapper
        passwordinp = input("How is your password? ")
        if passwordin == passwordinp:
            return func()
        else:
            print("Is not correct the password")
    return wrapper

@password_required
def needs_password():
    print("Is correct the password")


def uppr(func):
    def wrapper(*args, **kwargs): #Argumentos con keywords, con nombre o posicionales, el asterisco es una expansión
        result = func(*args,**kwargs)
        return result.upper()
    return wrapper #Siempre retorna el wrapper

    
@uppr
def say_my_name(name):
    print(f"Hola, {name}")
    return name

if __name__ == '__main__':
    say_my_name(input("How is your name? "))
    needs_password()


"""

def func_decorator(function_parameter): #Se crea función decoradora que recibe otra función
    def interior_function(): #Wrapper también llamada función C
        #Acciones adicionales que decoran
        print("I\'ll perform a calculation: ")
        function_parameter()
        print("I did the calculation")
    return interior_function #Se devuelve siempre la función interior

@func_decorator #Se escribe esta sintaxis antes de la función que se quiere decorar
def addition():
    print(15+15)

@func_decorator
def subtraction():
    print(15+15)
    
addition()
subtraction()
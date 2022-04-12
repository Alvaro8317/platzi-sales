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
    def interior_function(*args, **kwargs): # Con el *args se indica que puede recibir x parametros # kwargs son para parametros llave vs
        #Acciones adicionales que decoran
        print("I\'ll perform a calculation: ")
        function_parameter(*args, **kwargs) #Se debe de indicar el args aquí también
        print("I did the calculation")
    return interior_function #Se devuelve siempre la función interior

@func_decorator #Se escribe esta sintaxis antes de la función que se quiere decorar
def addition(a,b,c):
    print(a+b+c)

@func_decorator
def subtraction(a,b,c):
    print(a-b-c)

@func_decorator
def squaring(base,exponent):
    print(pow(base,exponent))

a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
addition(a,b,c)
subtraction(a,b,c)
squaring(base=a,exponent=b)
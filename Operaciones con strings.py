platzi = 'platzi'.upper()
print(platzi.find('zi'.upper()))
print(platzi.startswith('p'.upper()))
print(dir(platzi)) #Muestra los dunder methods, que son los que inician con __ y terminan con __
# Dunder methods sirven para modificar como python se ejecuta
# https://docs.python.org/3/reference/datamodel.html#special-method-names

def my_function():
    """Este es un texto ayuda de como ejecutar la función '\my function'\ """
    pass
comm = input()
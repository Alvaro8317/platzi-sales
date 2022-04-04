#Cambio en listas
countries = ['Colombia','Mexico','Venezuela','Argentina','']
global_countries = countries #Apunta al mismo espacio de memoria, por lo que si se modifica una, modificará la otra
#Copy
global_countries = None
global_countries = countries.copy()
global_countries[4] = 'Perú'
print (f"Variable countries: {countries}, variable global: {global_countries}")
#Otra forma de copiar
lista = [1, 2, 3, 4, 5]
mi_lista = lista[:]
print (f"Lista: {lista}, mi_lista: {mi_lista}")
mi_lista[4] = 10
print (f"Lista: {lista}, mi_lista: {mi_lista}")
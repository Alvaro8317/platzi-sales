a = 1,2,3
print(type(a))
a = (1,2,3) #Se pueden inicializar de las dos formas
print(type(a))
a = (1,1,1,2,3,4,5)
print(a.count(1)) #Retorna cuantas veces hay este valor
print(a.index(2)) #Retorna en que index está ubicado por primera vez este valor
a = set([1,2,3])
print(type(b))
b = {3,4,5}
print(type(b)) #Se puede inicializar de las dos formas, con diferencia a los diccionarios que los set no tienen llaves
#Los set no soportan índices, porque estos no tienen un orden específico.
b.add(3)
print(b) #No soporta duplicados
b.add(20)
print(b) #Al no ser duplicado, lo inserta
print(a.intersection(b)) #Diagramas de Benn, parecidos a los JOIN en SQL
print(a.union(b))
print(a.difference(b))
print(a.difference(b))
b.remove(20)
A = {1, 2, 3}	# conjunto A
B = {3, 4 ,5}	# conjunto B
print(A | B)	# unión
print(A & B)	# intersección
print(A - B)	# diferencia entre A y B
print(B - A)	# diferencia entre B y A
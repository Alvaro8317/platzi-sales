"""
list_num = list(range(100))
pares = [number for number in list_num  if number % 2 == 0] #List comprehension
print(pares)
student_uid = [1,2,3]
students = ['Juan','Jose','Larsen']
students_relation = {uid : stu for uid, stu in zip(student_uid,students)} # La función zip regresa un iterador de tuplas | Dict comprehension
print(students_relation)
import random
random_num = []
for i in range (10):
    random_num.append(random.randint(1,3))
print(random_num)
not_repeted = {number for number in random_num} # Set comprehension
print(not_repeted)
"""
# -------------------------------------------------- EXERCICES --------------------------------------------------
# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""
ex_a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
listeven = [number for number in ex_a if number % 2 == 0]
print(listeven)
"""
# Take two lists, say for example these two:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes.
"""
import itertools


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
newset = set()
for i in a:
    for j in b:
        if i == j:
            newset.add(i)
        else:
            continue
print(newset)
print(list(itertools.zip_longest(a,b, fillvalue='Nada')))
# Now with set comprehensions
new_set2 = (set(a[x] for x in range(len(a)) if a[x] in b))
print(new_set2)

# Find all of the numbers from 1-1000 that are divisible by 7
print("-" * 79 + "EXERCISE 1" + "-" * 79)
print(list(a for a in range(1,1001) if a%7 == 0))
# Find all of the numbers from 1-1000 that have a 3 in them
print("-" * 79 + "EXERCISE 2" + "-" * 79)
print(list(a for a in range(1,1001) if '3' in str(a)))
#Count the number of spaces in a string
print("-" * 79 + "EXERCISE 3" + "-" * 79)
inp= str(input("Please insert a sentence and I told you how many spaces are in that sentence: "))
print(len(list(a for a in inp if a == ' ')))
"""
# Create a list of all the consonants in the string “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams”
import string
print("-" * 79 + "EXERCISE 4" + "-" * 79)
stringex4 = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams, special characters: * \' and ()/"
#print(list (a for a in stringex4 if a not in ('a','e','i','o','u', ' '))) Does'nt work very well with special characters
print(list (a for a in stringex4 if a not in ('a','e','i','o','u', ' ') and (a in list(string.ascii_lowercase) or a in list(string.ascii_uppercase)) ) )
# Get the index and the value as a tuple for items in the list
# “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’). Result would look like (index, value), (index, value)
print("-" * 79 + "EXERCISE 5" + "-" * 79)
items = ["hi", 4, 8.99, 'apple', ('t,b','n')]
print ( [(index, item) for index, item in enumerate(items)] )
# Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5
print("-" * 79 + "EXERCISE 6" + "-" * 79)
list_a = 1, 2, 3, 4 , 4
list_b = 2, 3, 4, 5
print (list (a for a in list_a if a in list_b) ) #Can return repeated numbers, so I used better a set
print (set (a for a in list_a if a in list_b) )
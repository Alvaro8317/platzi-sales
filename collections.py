# - :link: [collections — Container datatypes](https://docs.python.org/3/library/collections.html)

# El módulo collections nos brinda un conjunto de objetos primitivos que nos permiten extender el comportamiento de las built-in collections que poseé Python y nos otorga estructuras de datos adicionales. Por ejemplo, si queremos extender el comportamiento de un diccionario, podemos extender la clase UserDict; para el caso de una lista, extendemos UserList; y para el caso de strings, utilizamos UserString.

# 1. `namedtuple()` factory function for creating tuple subclasses with named fields
# 2. `deque` list-like container with fast appends and pops on either end
# 3. `ChainMap` dict-like class for creating a single view of multiple mappings
# 4. `Counter` dict subclass for counting hashable objects
# 5. `OrderedDict` dict subclass that remembers the order entries were added
# 6. `defaultdict` dict subclass that calls a factory function to supply missing values
# 7. `UserDict` wrapper around dictionary objects for easier dict subclassing
# 8. `UserList` wrapper around list objects for easier list subclassing
# 9. `UserString` wrapper around string objects for easier string subclassing


# ##### Counter
# ```python
# from collections import Counter
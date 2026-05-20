#Tuples

# Creating tuples (immutable)
empty_tuple = ()
point = (10, 20)
single_item = (5,)  # Comma is necessary
coordinates = (1, 2, 3)

# Accessing tuple elements
x, y, z = coordinates  # Tuple unpacking
print(x, y, z)         # 1 2 3
print(point[0])        # Indexing: 10
print(point[-1])       # Negative: 20

# Tuple methods
colors = ("red", "green", "blue", "red")
print(colors.count("red"))  # 2
print(colors.index("blue")) # 2

# Named tuples
from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "city"])
alice = Person("Alice", 30, "New York")
print(alice.name, alice.age, alice.city)
print(alice[0])  # Access by index

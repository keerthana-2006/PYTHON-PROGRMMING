#Object-Oriented Programming
#Explanation: OOP organizes code using classes and objects, promoting code reuse and modularity.

#Classes and Objects

# Basic class definition
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    
    def description(self):
        return f"{self.name} is {self.age} years old"

# Creating objects (instances)
buddy = Dog("Buddy", 3)
max = Dog("Max", 5)

print(buddy.name)          # Buddy
print(buddy.bark())        # Buddy says Woof!
print(buddy.species)       # Canis familiaris
print(max.description())   # Max is 5 years old

# Modifying attributes
buddy.age = 4
print(buddy.age)  # 4

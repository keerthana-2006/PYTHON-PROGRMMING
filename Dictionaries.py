#Dictionaries

# Creating dictionaries
empty_dict = {}
person = {"name": "John", "age": 30, "city": "Boston"}
person2 = dict(name="Jane", age=25, city="Chicago")

# Accessing values
print(person["name"])           # John
print(person.get("age"))        # 30
print(person.get("country", "USA"))  # Default: USA

# Modifying dictionaries
person["age"] = 31              # Update value
person["email"] = "john@example.com"  # Add new key
person.update({"phone": "123-456", "age": 32})  # Multiple updates

# Removing items
del person["city"]              # Delete key
age = person.pop("age")         # Remove and return
last_item = person.popitem()    # Remove and return last item
person.clear()                  # Clear all

# Dictionary methods
person = {"name": "Alice", "age": 30}
print(person.keys())     # dict_keys(['name', 'age'])
print(person.values())   # dict_values(['Alice', 30])
print(person.items())    # dict_items([('name', 'Alice'), ('age', 30)])

# Looping through dictionaries
for key in person:
    print(key, person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Default dictionary
from collections import defaultdict

word_count = defaultdict(int)
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
for word in words:
    word_count[word] += 1
print(dict(word_count))  # {'apple': 3, 'banana': 2, 'orange': 1}

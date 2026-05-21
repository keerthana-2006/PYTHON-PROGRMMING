8. String Manipulation
Explanation: Strings are sequences of characters that support various operations for text processing.

String Creation and Basic Operations
python
# String creation
single_quote = 'Hello'
double_quote = "World"
triple_quote = """This can span
multiple lines"""
raw_string = r"C:\Users\Name"  # Raw string (no escape)

# String concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # "Hello World"

# String repetition
print("Ha" * 3)  # "HaHaHa"

# String length
text = "Python"
print(len(text))  # 6

# Indexing and slicing
text = "Python Programming"
print(text[0])      # 'P'
print(text[-1])     # 'g'
print(text[0:6])    # 'Python'
print(text[7:])     # 'Programming'
print(text[::-1])   # Reverse: 'gnimmargorP nohtyP'

# String methods
text = "  Hello, World!  "
print(text.strip())          # Remove whitespace: "Hello, World!"
print(text.lower())          # Lowercase
print(text.upper())          # Uppercase
print(text.capitalize())     # Capitalize first letter
print(text.title())          # Title case
print(text.replace("World", "Python"))  # Replace substring
print(text.split(","))       # Split into list: ['  Hello', ' World!  ']
print(" ".join(["Hello", "World"]))  # Join: "Hello World"

# Finding substrings
text = "Python is awesome"
print(text.find("is"))       # Index: 7
print(text.find("not"))      # -1 (not found)
print(text.index("is"))      # 7 (error if not found)
print("is" in text)          # True
print(text.count("a"))       # 1

# String formatting
name, age = "Alice", 30
# Old style (%)
print("Name: %s, Age: %d" % (name, age))
# format() method
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))
# f-strings (Python 3.6+)
print(f"Name: {name}, Age: {age}")
print(f"Age in 5 years: {age + 5}")

# String validation methods
text = "Python123"
print(text.isalpha())  # False (has numbers)
print(text.isalnum())  # True (letters and numbers)
print(text.isdigit())  # False
print(text.islower())  # False
print(text.isupper())  # False
print("   ".isspace()) # True

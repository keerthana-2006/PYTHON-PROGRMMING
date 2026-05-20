#Lists
# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# List operations
fruits = ["apple", "banana", "orange"]
print(len(fruits))           # Length: 3
print(fruits[0])             # Indexing: apple
print(fruits[-1])            # Negative indexing: orange
print(fruits[1:3])           # Slicing: ['banana', 'orange']

# Modifying lists
fruits[0] = "grape"          # Change element
fruits.append("kiwi")        # Add to end
fruits.insert(1, "mango")    # Insert at index
fruits.extend(["pear", "plum"])  # Extend list
fruits.remove("banana")      # Remove by value
popped = fruits.pop()        # Remove and return last
popped_index = fruits.pop(0) # Remove at index
del fruits[1]                # Delete by index

# List methods
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()               # Sort in-place
numbers.reverse()            # Reverse in-place
print(numbers.count(1))      # Count occurrences: 2
print(numbers.index(4))      # Find index: 2
numbers.clear()              # Clear all elements

# Copying lists
original = [1, 2, 3]
shallow_copy = original.copy()  # or original[:]
deep_copy = original[:]      # For nested lists, use copy.deepcopy()

# List concatenation and repetition
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)         # [1, 2, 3, 4]
print(list1 * 3)             # [1, 2, 1, 2, 1, 2]

# Creating sets (unordered, unique)
empty_set = set()  # Not {}
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14}
from_list = set([1, 2, 2, 3, 3, 4])  # {1, 2, 3, 4}

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a | set_b)   # Union: {1, 2, 3, 4, 5, 6}
print(set_a & set_b)   # Intersection: {3, 4}
print(set_a - set_b)   # Difference: {1, 2}
print(set_a ^ set_b)   # Symmetric difference: {1, 2, 5, 6}

# Set methods
set_a.add(7)           # Add element
set_a.update([8, 9])   # Add multiple
set_a.remove(9)        # Remove (error if not present)
set_a.discard(10)      # Remove (no error if not present)
set_a.pop()            # Remove arbitrary element
set_a.clear()          # Clear all

# Set comparisons
print({1, 2}.issubset({1, 2, 3}))  # True
print({1, 2, 3}.issuperset({1, 2})) # True
print({1, 2}.isdisjoint({3, 4}))   # True

# Frozenset (immutable set)
immutable_set = frozenset([1, 2, 3])

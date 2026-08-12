# ==============================================================================
# Topic: Data Structures - Sets & Set Operations
# Level: Foundational
# Description: Unordered collections, unique elements, and common set methods.
# ==============================================================================

# Defining a Set (Unordered, Unique values)
my_set = {"ahmed", "hassan", "ali", (1, 2, 3)}
print("Original Set:", my_set)

print("=" * 50)

# Essential Set Methods
set_a = {1, 2, 3}
set_b = {4, 5, 6}

# Combining sets using union()
combined_set = set_a.union(set_b)
print("Union of Set A and Set B:", combined_set)

# Adding and Removing elements
set_a.add(10)
set_a.discard(1)  # Removes element safely without raising an error if missing
print("Updated Set A:", set_a)

# Clearing all elements
set_a.clear()
print("Cleared Set A:", set_a)
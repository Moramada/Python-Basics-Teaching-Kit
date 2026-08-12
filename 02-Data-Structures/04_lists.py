# ==============================================================================
# Topic: Data Structures - Lists & List Methods
# Level: Foundational
# Description: Demonstrating list indexing, nested elements, and built-in methods.
# ==============================================================================

# 1. Defining a List with Mixed Data Types & Nested Lists
mixed_list = ["Ahmed", 1, True, False, 10.5, [1, 2, 3, [4, 5, 6, 7]]]

print("Original List:", mixed_list)
print("Accessing Index 3:", mixed_list[3])
print("Accessing Nested Element (7):", mixed_list[5][3][3])

# Updating elements in a list (Mutable)
mixed_list[0] = "Muhammed"
print("Updated List:", mixed_list)

print("=" * 50)

# 2. Essential List Methods
numbers = [5, 2, 3]

numbers.insert(0, 10)       # Insert at specific index
numbers.append(99)          # Add element to the end
numbers.remove(10)          # Remove specific value
print("Modified Numbers List:", numbers)

# Combining Lists
list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_a.extend(list_b)
print("Extended List:", list_a)

# Sorting Lists
unsorted_list = [9, 5, 7, 8, 2]
unsorted_list.sort()
print("Ascending Order:", unsorted_list)

unsorted_list.sort(reverse=True)
print("Descending Order:", unsorted_list)
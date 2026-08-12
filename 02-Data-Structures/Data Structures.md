# 02. Data Structures in Python

This directory covers primary Python collection data types used for organizing and manipulating structured data. Designed with practical teaching examples for foundational tracks.

---

## Concepts Covered

| Topic | File Name | Key Concepts Introduced |
| :--- | :--- | :--- |
| Lists | 01_lists.py | Ordered & mutable collections, indexing, slicing, nested lists, and list methods. |
| Tuples | 02_tuples.py | Ordered & immutable structures, fixed datasets, and tuple vs list comparisons. |
| Sets | 03_sets.py | Unordered collections, unique values, and set operations (union, add, discard). |
| Dictionaries | 04_dictionaries.py | Key-Value structures, dynamic lookup, value updates, and dictionary methods. |

---

## Instructor Notes & Common Edge Cases

When introducing data structures to students, standard pitfalls are explicitly addressed in lessons:

### 1. Mutability vs Immutability
_ Common Issue: Attempting to modify element values in a Tuple directly (e.g., tuple[0] = value).
_ Resolution: Highlighting TypeError exceptions and clarifying use-case scenarios for immutable data.

### 2. Key Errors in Dictionaries
_ Common Issue: Accessing non-existent dictionary keys directly causing KeyError exceptions.
_ Resolution: Teaching defensive coding using the .get() method or pre-checking keys.

### 3. Duplicate Elements in Sets
_ Common Issue: Confusion when duplicate items automatically disappear in Sets.
_ Resolution: Demonstrating unique value collection through real-world scenarios.

---

## Practice Tasks Included
_ Modifying dynamic product inventory lists.
_ Storing fixed spatial coordinates using Tuples.
_ Eliminating duplicates from user-submitted inputs using Sets.
_ Building item price lookup maps using Dictionaries.
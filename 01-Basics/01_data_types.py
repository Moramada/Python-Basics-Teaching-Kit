# ==============================================================================
# Topic: Python Data Types
# Level: Foundational
# Description: Exploring primitive data types and type checking using type().
# ==============================================================================

# Checking data types using type()
print("Data Type of 'Apple':", type("Apple"))      # str (String)
print("Data Type of 17:", type(17))               # int (Integer)
print("Data Type of 17.5:", type(17.5))           # float (Floating Point)
print("Data Type of [1, 2, 3]:", type([1, 2, 3])) # list (List)
print("Data Type of (2 == 2):", type(2 == 2))     # bool (Boolean)

print("=" * 50)

# Examples of different Python Data Structures & Types
print("Integer Example:", type(100))
print("Float Example:", type(100.9))
print("String Example:", type("Hello Python"))
print("Tuple Example:", type((1, 2, 3)))
print("Dictionary Example:", type({"One": 1, "Two": 2}))
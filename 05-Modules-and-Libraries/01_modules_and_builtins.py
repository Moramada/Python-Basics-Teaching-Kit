# ==============================================================================
# Topic: Python Standard Modules & Libraries
# Level: Foundational / Intermediate
# Description: Practical examples covering math, random, datetime, sys, and os modules.
# ==============================================================================

import math
import random
import datetime
import sys
import os

# 1. Math Module (Math Calculations)
print("--- 1. Math Module ---")
print("Power (2^3):", math.pow(2, 3))
print("Square Root (25):", math.sqrt(25))
print("Ceil (3.1):", math.ceil(3.1))        # Rounds up
print("Floor (3.9):", math.floor(3.9))      # Rounds down
print("Factorial (5!):", math.factorial(5))

# 2. Random Module (Randomness & Selection)
print("\n--- 2. Random Module ---")
print("Random Float (0 to 1):", random.random())
print("Random Int (1 to 100):", random.randint(1, 100))

items = ["Python", "Java", "C++", "JavaScript"]
print("Random Choice:", random.choice(items))

random.shuffle(items)
print("Shuffled List:", items)

# 3. Datetime Module (Dates & Time)
print("\n--- 3. Datetime Module ---")
now = datetime.datetime.now()
print("Current Date & Time:", now)
print("Formatted Date:", now.strftime("%Y-%m-%d %H:%M:%S"))
print("Current Year:", now.year)

# 4. OS Module (Operating System & Files)
print("\n--- 4. OS Module ---")
print("Current Directory:", os.getcwd())
print("Directory Contents:", os.listdir('.'))

# 5. Sys Module (System Information)
print("\n--- 5. Sys Module ---")
print("Python Version:", sys.version.split()[0])
print("Platform:", sys.platform)
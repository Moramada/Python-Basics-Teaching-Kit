# ==============================================================================
# Topic: For Loops & Iteration
# Level: Foundational
# Description: Detailed examples covering range variants, list processing, and loop control statements.
# ==============================================================================

# 1. Basic Range Iteration (Single Parameter)
print("--- 1. Range with 1 Parameter (0 to N-1) ---")
for i in range(5):
    print("Step:", i)

# 2. Range with Start and Stop Parameters
print("\n--- 2. Range with Start and Stop ---")
for i in range(1, 6):
    print("Number:", i)

# 3. Range with Step Parameter
print("\n--- 3. Range with Custom Step (Even Numbers) ---")
for i in range(2, 11, 2):
    print("Even Number:", i)

# 4. Iterating Through a List & Accumulation
print("\n--- 4. List Iteration & Accumulator Pattern ---")
prices = [10, 20, 30, 40]
total = 0

for price in prices:
    print("Item Price:", price)
    total += price

print("Total Bill Amount:", total)

# 5. Using Loop Control: 'continue' (Skip Current Iteration)
print("\n--- 5. Using 'continue' to Skip Odds ---")
for num in range(1, 6):
    if num % 2 != 0:
        continue  # Skip odd numbers
    print("Processed Even Number:", num)

# 6. Using Loop Control: 'break' (Stop Loop Early)
print("\n--- 6. Using 'break' for Early Exit ---")
for num in range(1, 10):
    if num == 5:
        print("Target 5 found! Stopping loop.")
        break
    print("Checking number:", num)
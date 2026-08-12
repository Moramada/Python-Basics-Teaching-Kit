# ==============================================================================
# Topic: While Loops & Dynamic Iteration
# Level: Foundational
# Description: Demonstrating condition-based loops, counter variables, and input loops.
# ==============================================================================

# 1. Simple Counter-Based Loop
print("--- 1. Basic Counter Loop ---")
counter = 1

while counter <= 5:
    print("Counter Value:", counter)
    counter += 1  # Incrementing counter to avoid infinite loop

# 2. Input Validation Loop with Attempt Limits
print("\n--- 2. User Input Validation Loop ---")
secret_word = "python"
user_guess = ""

while user_guess != secret_word:
    user_guess = input("Guess the secret word: ").lower()
    if user_guess != secret_word:
        print("Wrong guess! Try again.")

print("Congratulations! You guessed correctly.")

# 3. While Loop with Else Clause
print("\n--- 3. While Loop with Else ---")
count = 1
while count <= 3:
    print("Count:", count)
    count += 1
else:
    print("Loop finished successfully without break!")
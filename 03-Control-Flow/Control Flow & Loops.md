# 03. Control Flow & Loops in Python

This directory covers iteration mechanisms in Python, focusing on definite iteration (For Loops) and condition-driven iteration (While Loops). Designed to train learners on repetitive logic and state accumulation.

---

## Concepts Covered

| Topic | File Name | Key Concepts Introduced |
| :--- | :--- | :--- |
| For Loops | 01_for_loops.py | Definite loops, iterating over lists/ranges, and accumulator patterns. |
| While Loops | 02_while_loops.py | Indefinite loops, conditional termination, and interactive input validation. |

---

## Instructor Notes & Common Edge Cases

When teaching loops to beginners, standard pitfalls are explicitly addressed in lessons:

### 1. Infinite Loops
_ Common Issue: Forgetting to update the loop condition variable inside a while loop, causing infinite execution.
_ Resolution: Teaching loop control variables and tracking counter progression visually.

### 2. Off-by-One Errors in range()
_ Common Issue: Expecting range(1, 5) to include the upper bound 5.
_ Resolution: Emphasizing Python's 0-indexed nature and exclusive upper bounds in range().

---

## Practice Tasks Included
_ Building dynamic PIN validation security prompts.
_ Calculating running totals and list item summaries using loops.
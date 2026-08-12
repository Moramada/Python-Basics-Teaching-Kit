# 04. Functions in Python

This directory introduces modular programming using functions. It covers function declaration, parameter passing, return values, and scope basics to write reusable code.

---

## Concepts Covered

| Topic | File Name | Key Concepts Introduced |
| :--- | :--- | :--- |
| Functions Basics | 01_functions_basics.py | Function declaration (def), calling functions, parameters vs arguments, default parameters, and return values. |

---

## Instructor Notes & Common Edge Cases

When teaching functions to beginners, standard failure points include:

### 1. Print vs Return
_ Common Issue: Confusing print() inside a function with returning a value using return.
_ Resolution: Demonstrating that return passes data back to the caller for further operations, while print() only outputs text to console.

### 2. Missing Arguments
_ Common Issue: Calling a function without supplying required positional arguments.
_ Resolution: Teaching default argument values (e.g., tax_rate=0.14) to prevent TypeError exceptions.

---

## Practice Tasks Included
_ Creating dynamic greeting utilities.
_ Building tax calculation functions with default rates.
_ Writing evaluation logic returning pass/fail statuses.
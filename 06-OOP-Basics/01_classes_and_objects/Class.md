# 06. Object-Oriented Programming (OOP) Basics

This directory covers foundational Object-Oriented Programming (OOP) concepts in Python. It teaches students how to transition from procedural scripts to structured, object-driven architectures using real-world analogies (Car Systems and Bank Accounts).

---

## Concepts Covered

| Topic | File Name | Key Concepts Introduced |
| :--- | :--- | :--- |
| Car Management System | 01_car_system.py | Class definition, __init__ constructor, self reference, instance attributes, methods, and dynamic property updates. |
| Bank Account System | 02_bank_account_system.py | State encapsulation, validation logic (insufficient balance), deposits, and withdrawals. |
| Practice Task | 03_oop_exercise.py | Hands-on assignment for students to construct a functional OOP program independently. |

---

## Instructor Notes & Common Edge Cases

When introducing Object-Oriented Concepts to foundational students:

### 1. Understanding 'self'
_ Common Issue: Confusion around why self must be passed as the first parameter in class methods.
_ Resolution: Explain self as an explicit pointer representing the current instance created in memory.

### 2. Method Execution Order
_ Common Issue: Attempting to call class methods directly without instantiating an object first.
_ Resolution: Emphasize that classes act as blueprints, while objects represent instantiated physical entities.

### 3. Direct Attribute Mutation vs Method Updates
_ Common Issue: Mutating obj.price directly instead of using methods like update_price() or apply_discount().
_ Resolution: Highlight method-driven state changes to lay groundwork for encapsulation principles.

---

## Program Execution Flowchart

_ Step 1: Define Class (Attributes & Methods)
_ Step 2: Create Objects (Instances)
_ Step 3: Call Methods (display_info, update_price, apply_discount)
_ Step 4: Validate State & Output Final Results
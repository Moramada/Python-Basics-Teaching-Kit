# Encapsulation & Data Hiding (التغليف وحماية البيانات)

This module covers the core concepts of **Encapsulation** in Python, focusing on protecting internal object states, controlling attribute access, and applying data validation logic using Getters and Setters.

---

##  Topics & Files Included

| File Name | Description | Key Concepts |
| :--- | :--- | :--- |
| `01_encapsulation_basics.py` | Introduction to access modifiers and controlled data access. | Public/Private Attributes (`__var`), Getters (`get_`), Setters (`set_`). |
| `02_encapsulation_challenges.py` | Real-world problem solving enforcing state boundary limits. | Input Validation, Condition Checking (Smartphone Battery & Smart AC). |

---

##  Key Takeaways for Students

1. **Private Attributes (`__var`)**: Prevents direct external modification from outside the class.
2. **Getters**: Provide read-only access to internal private variables safely.
3. **Setters**: Allow modifying private attributes strictly under custom boundary conditions (e.g., temperature between 16°C and 30°C, grade between 0 and 100).
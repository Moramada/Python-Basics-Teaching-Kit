# Integrated OOP Practice & Capstone Projects

This directory contains real-world applied mini-projects and the final capstone assignment. These projects combine all four core pillars of Object-Oriented Programming: **Classes, Encapsulation, Inheritance, and Polymorphism**.

---

## Included Projects Overview

| File Name | Project Title | Business Logic & Concept Combination |
| :--- | :--- | :--- |
| `01_smart_travel_card.py` | Smart Travel Card System | Manages card balance privatly, applies trip discounts based on card type (Student vs Adult). |
| `02_theme_park_tickets.py` | Theme Park Ticketing | Encapsulates ticket prices, calculates child rates and adult surcharges dynamically. |
| `03_smart_weight_scale.py` | Smart Weight Scale System | Protects net weight, calculates container tare weight deductions (Bags vs Boxes). |
| `04_mobile_line_system.py` | **Capstone Project**: Mobile Line Platform | Complete system for managing prepaid/postpaid call charging rates and balance tracking. |

---

## Architectural Checklist Demonstrated

1. **Encapsulation**: Private state variables (`__balance`, `__price`, `__net_weight`) accessed via Getters/Setters.
2. **Inheritance**: Specialized child classes extending general parent base models using clean OOP structures.
3. **Polymorphism**: Identical function calls (`pay_trip`, `calculate_price`, `calculate_weight`, `make_call`) producing specialized operations.
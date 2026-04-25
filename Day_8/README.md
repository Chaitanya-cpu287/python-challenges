# Smart Inventory Mutation Tracker

## Project Overview
This Python project simulates a warehouse inventory system where each product contains nested details such as price, stock, and supplier rating.

The program demonstrates how data behaves when copied using **shallow copy** and **deep copy**. It helps understand real-world data corruption issues in nested structures.

---

## Problem Statement
Write a Python program that:

- Stores inventory as a list of dictionaries
- Uses minimum 3 functions
- Creates shallow copy and deep copy
- Modifies copied data and tracks changes
- Uses loops, conditions, and dictionary operations
- Compares original and copied structures

---

## Inventory Data Format

```python
inventory = [
    {
        "item": "Laptop",
        "details": {
            "price": 50000,
            "stock": 10,
            "supplier_rating": 4.5
        }
    },
    {
        "item": "Phone",
        "details": {
            "price": 20000,
            "stock": 25,
            "supplier_rating": 4.3
        }
    }
]
```

---

## Functions Used

### 1. create_inventory()
Creates and returns inventory data.

### 2. apply_discount(data)
Applies changes only to selected product using:

```python
index = roll_number % len(data)
```

Changes:
- Reduces price by 10%
- Reduces stock by 5

### 3. compare_data(original, modified)
Compares both inventories and returns:

```python
(changed_items_count, unchanged_items_count)
```

---

## Custom Mutation Rule

Roll Number:

```python
24
```

Inventory Length:

```python
3
```

Calculation:

```python
24 % 3 = 0
```

Modified Product:

```python
Laptop
```

---

## Copy Analysis

## Shallow Copy
Shallow copy creates a new outer list, but nested dictionaries still use same memory references.

So modifying copied nested data also changes original inventory.

### Evidence:
If Laptop stock is changed in shallow copy, original Laptop stock also changes.

---

## Deep Copy
Deep copy creates fully separate nested objects.

So modifications remain only inside copied inventory.

### Evidence:
Changing Laptop price in deep copy does not affect original inventory.

---

## Final Output Includes

- Original Inventory
- Shallow Copy Result
- Deep Copy Result
- Differences Observed
- Tuple Summary

---

## Technologies Used

- Python 3
- copy module

---

## Learning Outcome

Through this project, I learned:

- Difference between shallow copy and deep copy
- Working with nested dictionaries
- Data mutation behavior
- Use of functions, loops, and conditions
- Real-world copying issues in data systems

---

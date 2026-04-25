# Academic Data Drift & Copy Behavior Analyzer

## Overview

This project is developed in Python to analyze student academic data and study the effects of shallow copy and deep copy.

The program generates random student records, stores them as nested dictionaries, converts them into a Pandas DataFrame, performs statistical analysis using NumPy, applies mathematical transformations, and detects data drift after mutation.

It also classifies the final system condition based on drift level and copy behavior.

---

## Problem Statement

Write a Python program that:

- Generates student data using random  
- Stores data as list of dictionaries (nested)  
- Converts data into a Pandas DataFrame  
- Uses NumPy for statistical analysis  
- Uses math functions for transformation  
- Applies shallow copy and deep copy  
- Implements minimum 4 functions  
- Detects data drift after mutation  

---

## Data Format

```python
{
    "id": int,
    "marks": int,
    "attendance": int,
    "scores": [internal, assignment]
}
```

---

## Processing Requirements

### Step 1: Data Generation

- Generate 10 to 15 students using random values

### Step 2: Copy Creation

Create:

- Shallow Copy  
- Deep Copy  

### Step 3: Mutation

Apply changes only on copied data:

```python
marks = marks + sqrt(marks)
```

Also:

- Modify inner list `scores`
- Change attendance for selected students

### Step 4: Analysis

Using NumPy and Pandas:

- Mean
- Median
- Standard Deviation

Detect drift:

```python
drift = abs(original_mean - modified_mean)
```

Normalize marks.

### Step 5: Pattern Detection

- Drift Alert → drift > threshold  
- Copy Failure → original data changed unexpectedly  
- Stable System → minimal variance  

---

## Personalization Applied

Roll Number Used: **549**

```python
549 % 3 = 0
```

Since result is 0, divisor was changed to **3**

Only indexes divisible by **3** were modified.

This rule was applied according to challenge instructions.

---

## Logic Used

1. Generated random student records using list of dictionaries.
2. Created shallow copy and deep copy.
3. Applied mutations only to copied data.
4. Used square root formula to increase marks.
5. Changed attendance and scores.
6. Used NumPy to calculate statistical values.
7. Used manual loop to calculate one metric without NumPy.
8. Compared original and modified mean to detect drift.
9. Checked whether shallow copy affected original data.
10. Classified system condition.

---

## Technologies Used

- Python  
- NumPy  
- Pandas  
- random  
- math  
- copy  

---

## Output Includes

- Original DataFrame  
- Shallow Copy Result  
- Deep Copy Result  
- Mean  
- Median  
- Standard Deviation  
- Manual Mean  
- Normalized Marks  
- Drift Value  

Tuple Output:

```python
(mean, drift, std_dev)
```

- Unique IDs using Set  
- Final Classification  

---

## Final Classification Types

- Stable Data  
- Minor Drift  
- Critical Drift  
- Copy Failure Detected  

---

## Why Shallow Copy Caused Drift

Shallow copy only copies the outer list.

Inner dictionaries and lists are still linked to the original object.

So when scores were changed inside shallow copy, the original data also changed unexpectedly.

---

## Why Deep Copy is Safe

Deep copy creates a completely separate copy of all nested objects.

Changes in copied data do not affect original data.

---

## Sample Formula Used

```python
new_marks = old_marks + math.sqrt(old_marks)
```

---

## What I Learned From This Challenge

- Difference between shallow copy and deep copy  
- Practical use of NumPy and Pandas  
- Data drift detection methods  
- Working with nested data structures  
- Random data generation  
- Statistical analysis using Python  
- Importance of copy behavior in real systems  


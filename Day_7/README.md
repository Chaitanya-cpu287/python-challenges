# Multi-Dimensional Academic Intelligence System

A Python-based academic analytics project that evaluates student performance using multiple factors such as marks, attendance, and assignment scores.

# Project Overview

This project generates student records, stores them in a structured format, classifies performance levels, and performs statistical analysis using Python libraries.

It helps understand how data can be analyzed in education systems using programming.

# Features

- Generate random student data
- Store records using lists and dictionaries
- Convert data into a Pandas DataFrame
- Calculate performance index
- Classify students into categories
- Perform statistical analysis
- Display tuple summary
- Show final academic system result

# Technologies Used

- Python
- :contentReference[oaicite:0]{index=0}
- :contentReference[oaicite:1]{index=1}
- Random Module
- Math Module

# Student Record Structure

Each student record contains:

- Student ID
- Marks
- Attendance
- Assignment Score
- Performance Index

# Performance Index Formula

(marks * 0.6 + assignment * 0.4) * log(attendance + 1)


# Functions Used

generate_data(n)
classify_students(data_frame)
analyze_data(data_frame)

# Sample Output

Enter number of students: 5

Student Data
(ID, Marks, Attendance, Assignment, Performance)

Categories
{'S1': 'Average', 'S2': 'Good'}

Mean = 58.2
Median = 60.0
Standard Deviation = 12.4

Tuple = (58.2, 12.4, 91)

Stable Academic System
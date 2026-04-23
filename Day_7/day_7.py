import random
import pandas as pd
import numpy as np
import math

def generate_data(n):
    student_list = []
    for i in range(1, n + 1):
        student_id = "S" + str(i)
        student_marks = random.randint(0, 100)
        student_attendance = random.randint(0, 100)
        student_assignment = random.randint(0, 50)
        performance_index = (student_marks * 0.6 + student_assignment * 0.4) * math.log(student_attendance + 1)
        student_list.append([student_id, student_marks, student_attendance, student_assignment, performance_index])
        
    return student_list

def classify_students(data_frame):
    category_dict = {}
    for i in range(len(data_frame)):
        student_id = data_frame["ID"][i]
        student_marks = data_frame["Marks"][i]
        student_attendance = data_frame["Attendance"][i]

        if student_marks < 40 or student_attendance < 50:
            category_dict[student_id] = "At Risk"
        elif student_marks <= 70:
            category_dict[student_id] = "Average"
        elif student_marks <= 90:
            category_dict[student_id] = "Good"
        else:
            category_dict[student_id] = "Top Performer"

    return category_dict

def analyze_data(data_frame):
    mean_marks = np.mean(data_frame["Marks"])
    median_marks = np.median(data_frame["Marks"])
    std_marks = np.std(data_frame["Marks"])
    max_marks = np.max(data_frame["Marks"])
    
    return mean_marks, median_marks, std_marks, max_marks

number_of_students = int(input("Enter number of students: "))
student_data = generate_data(number_of_students)
data_frame = pd.DataFrame(student_data, columns=["ID", "Marks", "Attendance", "Assignment", "Performance"])
print("Student Data")
print(data_frame)
student_category = classify_students(data_frame)
print("\nCategories")
print(student_category)
mean_marks, median_marks, std_marks, max_marks = analyze_data(data_frame)
print("Mean =", mean_marks)
print("Median =", median_marks)
print("Standard Deviation =", std_marks)
print("Tuple =", (round(float(mean_marks),2), round(float(std_marks),2), int(max_marks)))
if std_marks < 15:
    print("\nStable Academic System")
else:
    print("\nModerate Performance")
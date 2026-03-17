#  Student Marks Analyzer

##  Problem Overview
This program analyzes student marks and updates them based on a rule derived from the registration number. It then classifies each student's performance into categories like Excellent, Very Good, Good, Average, or Fail, and displays the total number of valid and failed students.

---

##  Features
- Accepts marks of multiple students  
- Takes registration number as input  
- Calculates sum of digits in registration number  
- Updates marks based on even/odd condition  
- Classifies student performance into categories  
- Counts number of valid and failed students  
- Displays updated marks and results  

---

##  Algorithm Explanation
I first collected marks of all students into a list. Then I took the registration number and calculated the sum of its digits. Based on whether the sum is even or odd, I updated all student marks by adding 8 or 10 respectively. After updating, I classified each student's marks into performance categories using conditional statements. Finally, I counted the number of students who passed and failed and displayed the results.

---

##  Personalized Logic
I used a rule-based logic where the update of marks depends on the parity (even or odd) of the sum of digits of the registration number. This adds a dynamic condition to the program. I also categorized student performance using ranges, which helps in better understanding of overall results.

---

##  Test Cases

### Test Case 1  
Input:  
Marks: [50, 60, 70]  
Registration Number: 1234  
Expected Output: Marks increased by 8 → [58, 68, 78]  
Classification: Average, Good, Very Good  

---

### Test Case 2  
Input:  
Marks: [30, 40, 90]  
Registration Number: 111  
Expected Output: Marks increased by 10 → [40, 50, 100]  
Classification: Average, Average, Excellent  

---

### Test Case 3  
Input:  
Marks: [20, 35, 80]  
Registration Number: 222  
Expected Output: Marks increased by 8 → [28, 43, 88]  
Classification: Fail, Average, Very Good  

---

##  Reflection: What logic decision did you make?
I decided to link the marks update with the registration number by using the sum of its digits. This makes the program dynamic and different from a fixed rule system. I also used clear classification ranges to evaluate student performance effectively.

---

##  How to Run
1. Run the Python program  
2. Enter number of students  
3. Enter marks for each student  
4. Enter registration number  
5. View updated marks and performance classification  

---

##  Technologies Used
Python (basic programming concepts)
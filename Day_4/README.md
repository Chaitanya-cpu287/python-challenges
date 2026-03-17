#  Student Risk Categorization System

##  Problem Overview
This program analyzes student marks and categorizes them into different risk levels such as Low, Medium, High, and Critical Risk. It also applies a personalized filtering rule based on the last digit of the registration number to remove certain risk categories.

---

##  Features
- Accepts marks of multiple students  
- Takes registration number as input  
- Categorizes marks into risk levels  
- Identifies invalid (negative) entries  
- Applies personalized filtering based on registration number  
- Displays categorized results and statistics  
- Counts valid, ignored, and removed entries  

---

##  Algorithm Explanation
I first collected marks of all students into a list and extracted the last digit of the registration number. Then I classified each mark into Low, Medium, High, or Critical Risk using conditional statements, while counting valid and invalid entries. After classification, I applied a personalized rule: if the last digit is even, Low Risk entries are removed; if odd, Critical Risk entries are removed. Finally, I displayed updated categories along with counts of valid, ignored, and removed entries.

---

##  Personalized Logic
I used a rule based on the last digit of the registration number to dynamically filter risk categories. If the digit is even, Low Risk students are removed, and if odd, Critical Risk students are removed. This adds personalization and makes the program adaptive instead of static.

---

##  Test Cases

### Test Case 1  
Input:  
Marks: [10, 40, 70, 110]  
Registration Number: 1234  
Expected Output:  
Low Risk removed → Medium, High, Critical remain  

---

### Test Case 2  
Input:  
Marks: [20, 50, 80, 120]  
Registration Number: 1235  
Expected Output:  
Critical Risk removed → Low, Medium, High remain  

---

### Test Case 3  
Input:  
Marks: [-5, 25, 65, 95]  
Registration Number: 2222  
Expected Output:  
Low Risk removed, one ignored entry  

---

##  Reflection: What logic decision did you make?
I decided to introduce personalization by using the last digit of the registration number to filter risk categories. This makes the program dynamic and different for each input. I also separated invalid entries to ensure proper classification and accurate counting.

---

##  How to Run
1. Run the Python program  
2. Enter number of students  
3. Enter registration number  
4. Enter marks for each student  
5. View categorized risk levels and filtered results  

---

##  Technologies Used
Python (basic programming concepts)
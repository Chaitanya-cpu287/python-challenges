#  Resource Demand Analyzer with PLI Filtering

##  Problem Overview
This program analyzes resource request values and categorizes them into Low, Moderate, and High demand levels. It also identifies invalid requests and applies a personalized filtering rule (PLI) based on the length of a name to remove certain categories of requests.

---

## ️ Features
- Accepts multiple resource request values  
- Categorizes requests into Low, Moderate, High demand, or invalid  
- Identifies zero demand separately  
- Stores categorized data in lists  
- Applies Personalized Logic Index (PLI) based filtering  
- Displays final categorized lists and statistics  

---

##  Algorithm Explanation
I first collected all resource request values into a list. Then I classified each request into Low, Moderate, High demand, or invalid using conditional statements. Zero values were treated as no demand. After classification, I calculated the length of a name and derived a PLI value using modulo operation. Based on the PLI value, I removed specific categories of requests. Finally, I displayed the updated lists and statistics.

---

##  Personalized Logic
I used a Personalized Logic Index (PLI) based on the length of a name. If PLI is 0, Low Demand requests are removed. If PLI is 1, High Demand requests are removed. Otherwise, multiple categories (Low, High, and Invalid) are removed. This makes the program dynamic and unique for different inputs.

---

##  Test Cases

### Test Case 1  
Input:  
Requests: [10, 25, 60, -5, 0]  
Name length = 9 → PLI = 0  
Expected Output:  
Low Demand removed  

---

### Test Case 2  
Input:  
Requests: [5, 30, 80, 15]  
Name length = 10 → PLI = 1  
Expected Output:  
High Demand removed  

---

### Test Case 3  
Input:  
Requests: [2, 22, 55, -3]  
Name length = 8 → PLI = 2  
Expected Output:  
Low, High, and Invalid removed  

---

##  Reflection: What logic decision did you make?
I introduced a personalized filtering mechanism using the length of a name to calculate a PLI value. This allowed the program to dynamically remove different categories of requests, making the logic more flexible and unique instead of using fixed rules.

---

##  How to Run
1. Run the Python program  
2. Enter number of resource requests  
3. Enter each request value  
4. View categorized lists and final results after PLI filtering  

---

##  Technologies Used
Python (basic programming concepts)
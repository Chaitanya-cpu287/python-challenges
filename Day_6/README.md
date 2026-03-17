
#  Smart Transaction Risk Detector

##  Problem Overview
This project analyzes a list of transaction amounts made by a user in a day and identifies suspicious spending patterns. Each transaction is categorized into normal, large, high-risk, or invalid based on its value. After classification, patterns are detected to determine the overall risk level as Low, Moderate, or High.

---

##  Features
- Accepts multiple transaction inputs from the user  
- Classifies transactions into different categories  
- Detects patterns like frequent transactions, large spending, and suspicious activity  
- Displays categorized transactions and summary  
- Determines final risk level  
- Uses Python concepts like lists, loops, dictionary, conditions, list comprehension, and tuple  

---

##  Algorithm Explanation
I collected all transaction amounts into a list and classified each transaction into normal, large, high-risk, or invalid using conditional statements. These categories were stored in a dictionary for organized access. Then, I calculated the total number of transactions and total spending amount. I checked three conditions: frequent transactions, large spending, and suspicious activity based on high-risk transactions. Based on these conditions, I determined the overall risk level. Finally, the program displays categorized transactions and the final risk classification.

---

##  Personalized Logic
I used a combination-based logic for risk classification where the final risk depends on how many conditions are satisfied. If all three conditions are true, the risk is High Risk. If any two conditions are true, it is Moderate Risk. Otherwise, it is Low Risk. This ensures that multiple suspicious patterns increase the severity of risk.

---

##  Test Cases

### Test Case 1  
Input: [100, 200, 300, 400]  
Expected Output: Low Risk  
Your Output: Low Risk  

### Test Case 2  
Input: [1000, 1500, 2000, 3000, 2500, 800]  
Expected Output: High Risk  
Your Output: High Risk  

### Test Case 3  
Input: [100, 600, 700, 2000, 300, 50]  
Expected Output: Moderate Risk  
Your Output: Moderate Risk  

---

##  Reflection: What logic decision did you make?
I used a combination-based decision approach where the risk level is determined by the number of conditions satisfied. Instead of relying on a single factor, I considered multiple conditions together to make the classification more reliable. I gave equal importance to all conditions, as the occurrence of multiple conditions indicates a higher chance of suspicious behavior.

---

##  How to Run
1. Run the Python program  
2. Enter the number of transactions  
3. Input each transaction amount  
4. View categorized transactions and final risk result  


# 🎓 Student Registration Validator

##  Problem Overview
This program validates student registration details such as student ID, email, password, and referral code. It checks whether each input follows specific formatting rules and determines whether the registration is approved or rejected.

---

##  Features
- Accepts student ID, email, password, and referral code  
- Validates student ID format (CSE-XXX)  
- Validates email structure with domain restriction (.edu)  
- Validates password strength (minimum length, uppercase start, contains digit)  
- Validates referral code format  
- Displays whether the registration is approved or rejected  

---

##  Algorithm Explanation
I collected user inputs such as student ID, email, password, and referral code. Then I applied nested conditional statements to validate each input step by step. The student ID is checked for correct format and numeric part. The email is validated for proper structure and domain. The password is checked for length, uppercase starting letter, and presence of digits. The referral code is validated based on its pattern. If all conditions are satisfied, the registration is approved, otherwise rejected.

---

##  Personalized Logic
I used a strict sequential validation approach where each condition must pass before checking the next. This ensures that invalid inputs are rejected immediately without unnecessary checks. I also added multiple conditions for password validation to improve security.

---

##  Test Cases

### Test Case 1  
Input:  
Student ID: CSE-123  
Email: student@college.edu  
Password: Password1  
Referral Code: REF12@  
Expected Output: APPROVED  
Your Output: APPROVED  

---

### Test Case 2  
Input:  
Student ID: CSE123  
Email: student@college.edu  
Password: Password1  
Referral Code: REF12@  
Expected Output: REJECTED  
Your Output: REJECTED  

---

### Test Case 3  
Input:  
Student ID: CSE-456  
Email: student@gmail.com  
Password: pass  
Referral Code: REF1@  
Expected Output: REJECTED  
Your Output: REJECTED  

---

##  Reflection: What logic decision did you make?
I decided to use nested validation where each input is verified step by step. I gave importance to format checking and security conditions, especially for password validation. This ensures that only properly structured and secure data is accepted.

---

##  How to Run
1. Run the Python program  
2. Enter student ID, email, password, and referral code  
3. View whether the registration is approved or rejected  

---

##  Technologies Used
Python (basic programming concepts)
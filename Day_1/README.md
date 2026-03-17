#  User Profile Validator

##  Problem Overview
This program validates user profile details such as name, email, mobile number, and age. It checks whether the entered information follows specific rules and determines whether the user profile is valid or invalid.

---

##  Features
- Takes user input for name, email, mobile number, and age  
- Validates name format (must contain space and proper structure)  
- Validates email format (must contain '@')  
- Validates mobile number (10 digits, numeric, valid starting digit)  
- Validates age (must be between 18 and 60)  
- Displays whether the user profile is valid or invalid  

---

##  Algorithm Explanation
I collected user inputs such as name, email, mobile number, and age. Then I applied conditional checks to validate each input. The name is checked for proper spacing and format. The email is checked for the presence of '@' and correct placement. The mobile number is validated for length, numeric values, and starting digit. The age is checked to be within a valid range. If all conditions are satisfied, the profile is marked as valid, otherwise invalid.

---

##  Personalized Logic
I used nested conditional statements to validate each field step by step. Each condition must be satisfied before moving to the next, ensuring strict validation. This approach helps in identifying invalid data early and ensures that all inputs follow the required format.

---

##  Test Cases

### Test Case 1  
Input:  
Name: John Doe  
Email: john@gmail.com  
Mobile: 9876543210  
Age: 25  
Expected Output: Valid  
Your Output: Valid  

---

### Test Case 2  
Input:  
Name: John  
Email: john@gmail.com  
Mobile: 9876543210  
Age: 25  
Expected Output: Invalid  
Your Output: Invalid  

---

### Test Case 3  
Input:  
Name: John Doe  
Email: johngmail.com  
Mobile: 12345  
Age: 17  
Expected Output: Invalid  
Your Output: Invalid  

---

##  Reflection: What logic decision did you make?
I decided to use step-by-step validation using nested conditions, where each input is checked in sequence. This ensures that the program stops validation as soon as an invalid condition is found, making the process efficient and reliable.

---

##  How to Run
1. Run the Python program  
2. Enter name, email, mobile number, and age  
3. View whether the user profile is valid or invalid  

---

##  Technologies Used
Python (basic programming concepts)
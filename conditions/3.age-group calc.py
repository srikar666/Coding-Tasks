# Age Group Categorizer
# Write a program that categorizes a person's age into different life stages based on the following conditions:
# 0-2 years: Infant
# 3-12 years: Child
# 13-19 years: Teenager
# 20-65 years: Adult
# Above 65 years: Senior
# The program takes an age as input and prints the age group category the person belongs to. 
# Sample Input 1:
# 15
# Sample Output 1:
# Teenager
# Sample Input 2: 
# 2
# Sample Output 2: 
# Infant
# Sample Input 3: 
# 72
# Sample Output 3: 

age = int(input("Enter the person's age: "))

if 0 <= age <= 2:
    category = "Infant"
elif 3 <= age <= 12:
    category = "Child"
elif 13 <= age <= 19:
    category = "Teenager"
elif 20 <= age <= 65:
    category = "Adult"
elif age > 65:
    category = "Senior"
else:
    category = "Invalid age"

print(f"The person is a {category}.")

#The f in print(f"...") denotes an f-string, which stands for formatted string literal.
# F-String: A string that starts with f or F and allows you to insert
#variables and expressions directly within the string.
#Inside the string, you can include variables or expressions within curly braces {},
#and Python will automatically replace them with their values.
# Grading System:
# Write a program that takes a student's score (out of 100) and outputs their grade based on the following conditions:
# 90-100: Grade A
# 80-89: Grade B
# 70-79: Grade C
# 60-69: Grade D
# Below 60: Grade F
# Sample Input 1: 
# 78
# Sample Output 1: 
# C
# Sample Input 2: 
# 90
# Sample Output 2: 
# A
# Sample Input 3: 
# 48
# Sample Output 3: 
# F
marks = int(input("Enter your obtained marks "))
if marks>=90 and marks<= 100:
  print("A")
elif marks>=80 and marks<= 89:
  print("B")
elif marks>=70 and marks<= 79:
  print("C")
elif marks >= 60 and marks <= 69:
  print("D")
elif marks < 60:
  print("F")
else:
    marks = print("Invalid marks")


exit()


# score = int(input("Enter the student's score (out of 100): "))

# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# elif 60 <= score < 70:
#     grade = "D"
# elif score < 60:
#     grade = "F"
# else:
#     grade = "Invalid score"
# print(f"The student's grade is: {grade}")

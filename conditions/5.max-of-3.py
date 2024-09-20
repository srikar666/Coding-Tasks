# Maximum of Three Numbers:
# Write a program that takes three numbers as input and prints the largest number.
# Sample Input 1: 
# 15 23 16
# Sample Output 1: 
# 23
# Sample Input 2: 
# 8 5 9
# Sample Output 2: 
# 9

number1 = int(input(),end="")
number2 = int(input(),end="")
number3 = int(input(),end="")


if number2<= number1 >= number3:
    largest = number1
elif number2 >= number1 and number2 >= number3:
    largest = number2
else:
    largest = number3


#print(f"the maximum number out of 3 numbe:{largest}")
print(largest)
# Write a program that takes a number n as input and prints all the factors of the number.
# Sample Input: 
# 24
# Sample Output: 
# 1 2 3 4 6 8 12 24
# Explanation: The factors of 24 are 1, 2, 3, 4, 6, 8, 12, 24.
n = int(input("Enter an integer n: "))
for i in range(1,n+1):
  if(n%i==0):
    print(i, end =" ")
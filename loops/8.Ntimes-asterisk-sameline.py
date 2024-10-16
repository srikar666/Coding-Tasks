#N times * in same line:
# You are given an integer n. Print * n times in the same line with space in between.
# Sample Input: 
# 5
# Sample Output: 
# * * * * *
# Input: user provides the number of times to print '*'
n = int(input("Enter the number of times to print '*': "))

for i in range(n):  
    if i < n : 
        print("*", end=" ") 
    else:
        print("*") 

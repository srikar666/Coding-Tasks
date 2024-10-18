# Write a program to calculate the factorial of a given number n. 
# The factorial of a number n is the product of all positive integers less than or equal to n.
# Sample Input: 
# 6
# Sample Output: 
# 720
# Explanation: 720 = 6*5*4*3*2*1
n=int(input())
mul=1
for i in range(1,n+1):
  mul*=i
print(mul)


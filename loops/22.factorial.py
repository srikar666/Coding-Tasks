# Write a program to calculate the factorial of a given number n. 
# The factorial of a number n is the product of all positive integers less than or equal to n.
# Sample Input: 
# 6
# Sample Output: 
# 720
# Explanation: 720 = 6*5*4*3*2*1

def factorial(n):
  if n==0:
    return 1
  else:
    return n*factorial(n-1)
print (factorial(5))
exit()



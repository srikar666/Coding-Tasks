# You are given an integer n. Print the sum of the first n terms of the series 3, 5, 7, 9, 11….
# Note: Use a loop instead of a mathematical formula.
# Sample Input: 
# 7
# Sample Output: 
# 63
# Explanation: Sum of 3+5+7+9+11+13+15 = 63

n=int(input())
sum=0
for i in range(n):
  values = 3+2*i
  print(values, end=" ")
  sum+=values
print( sum)




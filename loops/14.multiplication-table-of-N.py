# Multiplication Table of n:
# You are given an integer n. Print the multiplication table of n till count 10.
# Sample Input: 
# 7
# Sample Output: 
# 7 14 21 28 35 42 49 56 63 70
# Explanation: Print 7*1, 7*2, …, 7*10.
n = int(input("Enter an integer n: "))
c = int(input("Enter your count: "))
for i in range(1,c+1):
  print(i*n,end=" ")
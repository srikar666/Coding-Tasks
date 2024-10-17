# You are given an integer n. Print the first n odd numbers.
# Sample Input: 
# 7
# Sample Output: 
# 1 3 5 7 9 11 13
n = int(input("Enter an integer n: "))
for i in range(1,2*n,2):
  print(i,end=" ")
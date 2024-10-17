# You are given an integer n. Print the first n square numbers.
# Sample Input: 
# 7
# Sample Output: 
# 1 4 9 16 25 36 49
n = int(input("Enter an integer n: "))
for i in range(1,n+1):
  print(i*i,end=" ")
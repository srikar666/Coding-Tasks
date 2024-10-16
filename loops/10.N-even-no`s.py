#All Even Numbers till n:
# You are given an integer n. Print all the even numbers less than equal to n.
# Sample Input: 
# 14
# Sample Output: 
# 2 4 6 8 10 12 14
n = int(input("Enter a positive integer n: "))
for i in range(2,n+1,2):
  print(i,end="")

exit()

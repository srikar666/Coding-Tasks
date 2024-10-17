# First n Even Numbers:
# You are given an integer n. Print the first n even numbers.
# Sample Input: 
# 7
# Sample Output: 
# 2 4 6 8 10 12 14
n = int(input("Enter an integer n: "))
# i=2
# while i<n :

#   print(i,end=" ")
#   i=i+2
# exit()
for i in range(2, 2*n, 2):
  print(i,end = " ")


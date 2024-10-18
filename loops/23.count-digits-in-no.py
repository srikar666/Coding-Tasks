# Write a program that takes a number n as input and prints the number of digits the number has.
# Sample Input: 
# 1132
# Sample Output: 
# 4

def count(n):
  return(len(str(abs(n))));
n=int(input());
print(count(n))



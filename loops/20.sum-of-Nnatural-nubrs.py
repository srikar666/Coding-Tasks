# Sum of First n Natural Numbers:
# You are given an integer n. Print the sum of the first n Natural Numbers.
# Note: Use a loop instead of a mathematical formula.
# Sample Input: 
# 7
# Sample Output: 
# 28
# Explanation: Sum of 1+2+3+4+5+6+7 = 28
num=int(input())
sum=0;
while num>0:
  sum+=num
  num-=1
print(sum)
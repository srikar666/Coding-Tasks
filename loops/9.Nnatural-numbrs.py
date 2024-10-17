# First n Natural Numbers:
# You are given an integer n. Print the first n natural numbers.
# Sample Input: 
# 7
# Sample Output: 
# # 1 2 3 4 5 6 7

n = int(input("Enter a positive integer n: "))

for i in range(1, n + 1):
    if i < n: 
        print(i, end=" ")  
    else:
        print(i)  
exit()

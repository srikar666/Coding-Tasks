# Series: 2, 5, 8, 11, 14, …:
# You are given an integer n. Print first n terms of the series 2, 5, 8, 11, 14…
# Sample Input: 
# 7
# Sample Output: 
# 2 5 8 11 14 17 20
# Explanation: The series starts with 2 and every time adds 3 to get the next term.
n = int(input("Enter an integer n: "))
for i in range(2,2*n+3,3):
    #alterbative:for i in range(3, 3 + 2 * n, 2): 
    
    print(i, end =" ")
exit()
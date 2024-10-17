# Series: 3, 5, 7, 9, 11, …:
# You are given an integer n. Print first n terms of the series 3, 5, 7, 9, 11…
# Sample Input: 
# 7
# Sample Output: 
# 3 5 7 9 11 13 15
n = int(input("Enter an integer n: "))
for i in range(3,2*n+2,2):
    #alterbative:for i in range(3, 3 + 2 * n, 2): 
    
    print(i, end =" ")
exit()


# Series: 3, 6, 12, 24, 48, …:
# You are given an integer n. Print first n terms of the series 3, 6, 12, 24, 48…
# Sample Input: 
# 7
# Sample Output: 
# 3 6 12 24 48 96 192

n = int(input("Enter the number of terms (n): "))  

term=3
for i in range(n):
    print(term, end=" ") 
    term *=2  
    









# # All Square Numbers till n:
# # You are given an integer n. Print all the square numbers less than equal to n.
# # Sample Input: 
# # 50
# # Sample Output: 
# # 1 4 9 16 25 36 49
# n = int(input("Enter a number: "));
# for i in range(1,n+1,2):
# Input: user provides an integer n
n = int(input("Enter an integer n: "))
# i = 1
# while i * i <= n: 
#     print(i * i, end=" ") 
#     i += 1

# exit()
# for i in range(1,n+1):
#   if i*i<=n:
#     print (i * i, end=" ") 
#exit()
for i in range(1, int(n**0.5) + 1): 
    print(i * i, end=" ")
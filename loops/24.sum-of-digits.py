# Write a program that calculates the sum of all the digits in a given number n.
# Sample Input: 
# 1132
# Sample Output: 
# 7
# Explanation: 7 = 1+1+3d

def sum(n):
  
    n_str = str(n)
    
   
    total_sum = 0
    
    
    for digit in n_str:
        total_sum += int(digit) 
    return total_sum


print("Sum of digits:", sum_of_digits(n))
exit()
def sum_of_digits(n):
    total_sum = 0
    while n > 0:
        
        digit = n % 10
        
        total_sum += digit
        
        n = n // 10
    
    return total_sum  

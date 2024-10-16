# Sort Three Numbers
# Write a program that takes three numbers as input and prints the numbers in ascending order.
# This program doesn't use an array.
# Sample Input 1: 
# 15 23 16
# Sample Output 1: 
# 15 16 23
# Sample Input 2: 
# 8 5 9
# Sample Output 2: 
# 5 8 9
#__________________________________________________________________________________________
#The split() function in Python is used to break a string into parts (substrings),
#based on a specified separator (like spaces, commas, etc.). By default, it splits based on spaces.
#
#How split() works:
#If you don't provide a separator, split() uses spaces to break the string into separate words or numbers.
#It returns a list of the split parts.
#
#Yes, the output of the split() function is similar to a list because it actually returns a list! When you use split(),
#it breaks a string into smaller parts and stores them in a list.
#What is map() in Python?
#The map() function applies a specified function to each item of an input (like a list or any collection of data).
#It’s often used when you want to convert or transform multiple items in one go.

a,b,c = map(int,(input("enter the numers in same line by spaces:").split()));
if a>b:
  a,b=b,a;
if a>c:
  a,c = c,a;
if b>c:
  b,c = c,b;
print(a,b,c)
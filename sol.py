# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum

number1 = 70
number2 = 30

if number1*number2 < 1000 :
    result = number1 * number2
else :
    result = number1 + number2
print(result)

# Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

for i in range(1, 6):
    print()
    for j in range(0, i):
        print(i , end = "")


# Exercise 9: Check Palindrome Number
# Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forward and backward. For example, 545 is a palindrome number.

def check_palindrome_number(num):
    str_num = str(num)
    # reverse the string by slicing
    if str_num == str_num[::-1]:
        return True
    else:
        return False
print(check_palindrome_number(12321))

# Exercise 10: Merge two lists using the following condition
# Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

list3 = []
for i in list1:
    if i %2 != 0:
        list3.append(i)
for i in list2:
    if i %2 == 0:
        list3.append(i)
print(list3)

# Exercise 11: Get each digit from a number in the reverse order.
# For example, if the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

number = 7536
for i in str(number)[::-1]:
    print(i, end = " ")


# Exercise 12: Calculate income tax
# Calculate income tax for the given income by adhering to the rules below
# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
# Expected Output:
# For example, suppose the income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000

def income_tax(income):
    remaining_income = 0
    tax = 0
    if income > 10000:
        remaining_income = income - 10000
        if remaining_income > 10000 :
            remaining_income2 = remaining_income - 10000
            tax += 10000*10/100
            tax += remaining_income2 * 20/100
            return tax 
        tax = remaining_income *10/100
        return tax
    return tax
    
income = 15000
print(income_tax(income))

# Exercise 13: Print multiplication table from 1 to 10
# The multiplication table from 1 to 10 is a table that shows the products of numbers from 1 to 10.
# Write a code to generates a complete multiplication table for numbers 1 through 10.
# 1  2  3  4  5  6  7  8  9  10 
# 2  4  6  8  10 12 14 16 18 20 
# 3  6  9  12 15 18 21 24 27 30 
# 4  8  12 16 20 24 28 32 36 40 
# 5  10 15 20 25 30 35 40 45 50 
# 6  12 18 24 30 36 42 48 54 60 
# 7  14 21 28 35 42 49 56 63 70 
# 8  16 24 32 40 48 56 64 72 80 
# 9  18 27 36 45 54 63 72 81 90 
# 10 20 30 40 50 60 70 80 90 100 

for i in range(1, 11):                        
    for j in range(1, 11):
        if i*j > 9 :
            print(j*i, end=" ")
        else:
            print(j*i, end="  ")
    print()

# Exercise 14: Print a downward half-pyramid pattern of stars
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

for i in range(0, 6):                        
    for j in range(i, 6):
            print("*", end=" ")
    print()



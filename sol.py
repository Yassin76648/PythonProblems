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


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


# Exercise 15: Get an int value of base raised to the power of exponent
# Write a function called exponent(base, exp) that returns an int value of base raised to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.
def exp(base, exponent):
    if exponent < 0 :
        print("Sorry , exponent is negative")
    result = 1
    for i in range(1, exponent+1) :
        result *= base
    return result
print(exp(2, 5))


# Exercise 17: Generate Fibonacci series up to 15 terms
# Have you ever wondered about the Fibonacci Sequence? It’s a series of numbers in which the next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.
# Expected output:
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34  55  89  144  233  377
def fib(num):
    prev = 0
    current = 1

    for i in range(num):
        print(prev, " ") # 0 1
        next_fib = prev + current
        prev = current      # 1
        current =  next_fib  # 1 
fib(15)


# Exercise 18: Check if a given year is a leap year
# Rules for leap years: a year is a leap year if it’s divisible by 4, unless it’s also divisible by 100 but not by 400.
def leap_year(year):
    if year%4 == 0:
        if year%100 == 0 and year%400 != 0:
            return False
    else :
        return False
    return True
print(leap_year(2025))

# Exercise: 19: Print Alternate Prime Numbers till 20
# A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).
def prime_number(num):
    for i in range(2, num):
        is_prime = True
        for j in range(2, i):
            if i%j == 0:
                is_prime = False
                break
        if is_prime == True :
            print(i, end = " ")
prime_number(20)


# Exercise 20: Print Reverse Number Pattern
# Expected Output:
# 1 1 1 1 1 
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5 

for i in range(1, 6):
    for j in range(i, 6):
        print(i, end =" ")
    print()


# Exercise 21: Check if a user-entered string contains any digits using a for loop
def check_digits(string):
    for i in string:
        if i.isalpha():
            continue
        else:
            print("The string contains at least one digit.")
            break
        print("The string does not contain any digits.")

check_digits("Pynative123Python")

# Exercise 22: Capitalize the first letter of each word in a string
def capitalize(sentence):
    words = sentence.split()
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())
    new_sentence = " ".join(capitalized_words)
    return new_sentence

print(capitalize("The string does not contain any digits"))

# Convert Number TO Words 

def say_number(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("Out of range")

    ones = {
        0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
        5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }

    teens = {
        10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
        14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
        17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
    }

    tens = {
        20: "Twenty", 30: "Thirty", 40: "Forty", 50: "Fifty",
        60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
    }

    scales = ["", "Thousand", "Million", "Billion"]

    def say_0_to_999(n):
        words = []

        if n >= 100:
            words.append(ones[n // 100])
            words.append("Hundred")
            n %= 100

        if 10 <= n <= 19:
            words.append(teens[n])
        else:
            if n >= 20:
                words.append(tens[(n // 10) * 10])
                n %= 10
            if n > 0:
                words.append(ones[n])

        return " ".join(words)

    if number == 0:
        return "Zero"

    result = []
    scale_index = 0

    while number > 0:
        chunk = number % 1000
        if chunk != 0:
            words = say_0_to_999(chunk)
            if scales[scale_index]:
                words += " " + scales[scale_index]
            result.append(words)
        number //= 1000
        scale_index += 1

    return " ".join(reversed(result))


print(say_number(int(input("Enter number: "))))

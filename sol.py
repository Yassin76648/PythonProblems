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

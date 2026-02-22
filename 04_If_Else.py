#Conditional Statements (IF–ELIF–ELSE)
"""
Syntax 
if condition:
    # code
elif condition:
    # code
else:
    # code ###

"""

# 1. Check if a number is positive, negative, or zero

# positive
num = 12
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else :
    print("zero")

# negative    
num = -548
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else :
    print("zero")

# zero    
num = 0
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else :
    print("zero")


# 2. Find the largest of 3 numbers

num1 = 45
num2 = 78
num3 = 10

if num1 > num2:
    print("num1 is greater than num2")

elif num2 > num3:
    print("num2 is greater than num3")

else:
    print("num3 is greater than num2")

    
# 3. Check if a year is a leap year

year = 2026

if year % 400 == 0:
    print("leap year")
elif year % 100 == 0:
    print("not a leap year")
elif year % 4 == 0:
    print("leap year")
else:
    print("not a leap year")



# 4. Check if a number is divisible by 3 and 5

num = 50

if num % 3 == 0 and num % 5 == 0:
    print("number is divisible by both 3 and 5")
elif num % 3 == 0:
    print("number is divisible by 3")
elif num % 5 == 0:
    print("number is divisible by 5")
else:
    print("number is not divisible by 3 or 5")

# 5. Validate login:
#username == "admin"
#password == "1234"


username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")

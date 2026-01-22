## while_loops.py (examples + answers)


# 1. Print numbers from 10 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1


# 2. Sum of first N natural numbers
n = 5
total = 0
i = 1
while i <= n:
    total += i
    i += 1
print("Sum:", total)


# 3. Reverse a number
num = 1234
rev = 0
while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed:", rev)


# 4. Count digits in a number
num = 98765
count = 0
while num > 0:
    count += 1
    num //= 10
print("Digits:", count)


# 5. Palindrome check
num = 121
temp = num
rev = 0

while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10

if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

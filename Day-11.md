Python Arithmetic Operators Notes

Arithmetic operators are used to perform mathematical operations on numbers in Python.

Python supports the following arithmetic operators:
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Modulus (%)
Floor Division (//)
Exponentiation (**)

--------------------------------------------------
➕ 1. Addition Operator (+)

Used to add two numbers.

✅ Example:
a = 10
b = 5
print(a + b)

Output:
15

--------------------------------------------------
➖ 2. Subtraction Operator (-)

Used to subtract one number from another.

✅ Example:
a = 10
b = 5
print(a - b)

Output:
5

--------------------------------------------------
✖️ 3. Multiplication Operator (*)

Used to multiply two numbers.

✅ Example:
a = 10
b = 5
print(a * b)

Output:
50

--------------------------------------------------
➗ 4. Division Operator (/)

Performs normal division and always returns a float value.

✅ Example:
a = 10
b = 3
print(a / b)

Output:
3.3333333333333335

--------------------------------------------------
🔁 5. Modulus Operator (%)

Returns the remainder after division.

✅ Example:
a = 10
b = 3
print(a % b)

Output:
1

--> 10 divided by 3 gives remainder 1.

--------------------------------------------------
🔽 6. Floor Division Operator (//)

Returns the integer part of the division (removes decimal part).

✅ Example:
a = 10
b = 3
print(a // b)

Output:
3

--> It removes the decimal part.

--------------------------------------------------
🔼 7. Exponentiation Operator (**)

Used to calculate power.

✅ Example:
a = 2
b = 3
print(a ** b)

Output:
8

--> 2³ = 8

--------------------------------------------------
example
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print(f"The value of {a} + {b} is: {a + b}")
print(f"The value of {a} - {b} is: {a - b}")
print(f"The value of {a} * {b} is: {a * b}")
print(f"The value of {a} / {b} is: {a / b}")
print(f"The value of {a} % {b} is: {a % b}")
print(f"The value of {a} // {b} is: {a // b}")
print(f"The value of {a} ** {b} is: {a ** b}")

->> Important Note

If the second number (b) is 0:

Division (/)
Floor Division (//)
Modulus (%)

Will give an error: ZeroDivisionError

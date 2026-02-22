# Day 6: Python Functions

# 1. Simple function (no arguments, no return)
def greet():
    print("Hello! Welcome to Python Day 6.")

greet()


# 2. Function with one parameter
def greet_user(name):
    print("Hello,", name)

greet_user("Anusha")


# 3. Function with multiple parameters
def add_numbers(a, b):
    print("Sum:", a + b)

add_numbers(10, 20)


# 4. Function with return value
def multiply_numbers(a, b):
    return a * b

result = multiply_numbers(5, 4)
print("Multiplication Result:", result)


# 5. Function with default parameter
def greet_default(name="User"):
    print("Hello,", name)

greet_default()
greet_default("Anusha")


# 6. Function with condition (even or odd)
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("7 is", check_even_odd(7))
print("10 is", check_even_odd(10))


# 7. Function using loop
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)


# 8. Function to find sum of list elements
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

nums = [10, 20, 30, 40]
print("Sum of list:", sum_of_list(nums))


# 9. Function with eligibility check
def is_valid_user(age):
    if age >= 18:
        return "Eligible"
    else:
        return "Not Eligible"

print(is_valid_user(22))
print(is_valid_user(15))


# 10. Local vs Global variable example
x = 100  # Global variable

def variable_scope_demo():
    x = 50  # Local variable
    print("Inside function:", x)

variable_scope_demo()
print("Outside function:", x)


# 11. Function to print even numbers up to n
def print_even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            print(i)

print_even_numbers(10)


# 12. Function to calculate square of a number
def square(num):
    return num * num

print("Square of 6:", square(6))



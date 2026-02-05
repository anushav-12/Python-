# Syntax
for variable in sequence:
# code to repeat

"""
1. range() – Backbone of for Loop
🔹 range(start, stop, step)

start → where to begin (default = 0)
stop → where to stop (excluded)
step → jump (default = 1)

Examples:
range(5)          → 0,1,2,3,4
range(1, 6)       → 1,2,3,4,5
range(1, 10, 2)   → 1,3,5,7,9

-------------------------------------

Example 1: Print numbers 1 to 5
for i in range(1, 6):
    print(i)

Logic:
i takes value 1, prints, then 2, 3, 4, 5, stops before 6.
-------------------------------------
Example 2: Loop through a list
languages = ["Python", "SQL", "Java"]

for lang in languages:
    print(lang)
    
Logic:
lang = "Python"
then "SQL"
then "Java"
-------------------------------------
Example 3: Loop through a string
for ch in "Anusha":
    print(ch)
Logic:
for ch in "Anusha":
Python takes the string "Anusha"
Reads it one character at a time
Stores each character in the variable ch
Each character prints on a new line because print() adds a newline by default
---------------------------------------------------------------------------------
---------------------------------------------------------------------------------

2. for Loop with Conditions

Print even numbers from 1 to 20
for num in range(1, 21):
    if num % 2 == 0:
        print(num)

Logic:
% gives remainder
Even → remainder 0
-------------------------------------

3. break and continue
-> break → stop loop completely

for i in range(1, 10):
    if i == 5:
        break
    print(i)

Output:
1 2 3 4
-------------------------------------

4. continue → skip current iteration

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

Output:
1 2 4 5
-------------------------------------

5. Nested for Loops (Important for Interviews)
Example: Pattern logic
for i in range(3):
    for j in range(2):
        print(i, j)


Execution:
i=0 → j=0,1
i=1 → j=0,1
i=2 → j=0,1
-------------------------------------

6. while Loop (Condition-Based Loop)
-> What is while loop?
Runs as long as condition is TRUE

Syntax:
while condition:
    # code

Example 1: Print numbers 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1


Logic:
Check condition
Execute block
Update variable
Repeat

-- Forgetting i += 1 → infinite loop
-------------------------------------

7. Infinite Loop Example 
while True:
    print("Hello")


Used in:
Servers
Games
Continuous monitoring systems
-------------------------------------

8. while with break
i = 1
while True:
    if i == 6:
        break
    print(i)
    i += 1
-------------------------------------
    
"""

# FOR LOOP PRACTICE – QUESTIONS & ANSWERS

# Q1: Print numbers from 1 to 10
for i in range(1, 11):
    print(i)


# Q2: Print even numbers from 1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# Q3: Print odd numbers from 1 to 20
for i in range(1, 21):
    if i % 2 != 0:
        print(i)


# Q4: Print characters of a string
name = "Anusha"
for ch in name:
    print(ch)


# Q5: Sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i
print("Sum:", total)


# Q6: Multiplication table of 5
for i in range(1, 11):
    print("5 x", i, "=", 5 * i)


# Q7: Count vowels in a string
word = "python programming"
vowels = "aeiou"
count = 0

for ch in word:
    if ch in vowels:
        count += 1

print("Vowel count:", count)

print("Practice continues")


# Syntax
for variable in sequence:
# code to repeat

"""
range() – Backbone of for Loop
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


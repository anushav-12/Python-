"""
========================================
PYTHON STRING PRACTICE 
========================================

"""


# ========================================
# 1️⃣ BASIC VARIABLES & PRINTING
# ========================================

# Q1: Store your name and place in variables and print them.

name = "anu"
place = "blr"

print("Name:", name)
print("Place:", place)


# ========================================
# 2️⃣ STRING IMMUTABILITY
# ========================================

# Q2: Change first letter of "Anusha" to lowercase using slicing.

name = "Anusha"
new_name = "a" + name[1:]
print("Updated Name:", new_name)


# ========================================
# 3️⃣ STRING INDEXING
# ========================================

# Q3: Print last character of a string using negative indexing.

name = "Anusha"
print("Last character:", name[-1])


# ========================================
# 4️⃣ STRING SLICING
# ========================================

word = "Python"

# Q4: First 3 characters
print(word[0:3])   # Pyt

# Q5: First 4 characters
print(word[:4])    # Pyth

# Q6: From index 2 till end
print(word[2:])    # thon

# Q7: Every 2nd character
print(word[::2])   # Pto

# Q8: Reverse the string
print(word[::-1])  # nohtyP


# ========================================
# 5️⃣ CONCATENATION & REPETITION
# ========================================

# Q9: Join first and last name with space

first = "Anusha"
last = "V"

full = first + " " + last
print("Full Name:", full)

# Q10: Print "hi" 5 times

print("hi" * 5)


# ========================================
# 6️⃣ STRING METHODS
# ========================================

# Q11: Convert to uppercase, lowercase, and remove spaces

name = "  anusha"

print(name.upper())
print(name.lower())
print(name.strip())


# ========================================
# 7️⃣ SPLIT & JOIN
# ========================================

# Q12: Split string using comma

text = "hello,world,bye!"
print(text.split(","))

# Q13: Join list into sentence

words = ["Python", "is", "powerful"]
print(" ".join(words))


# ========================================
# 8️⃣ REPLACE METHOD
# ========================================

# Q14: Replace Java with Python

a = "I like Java"
print(a.replace("Java", "Python"))


# ========================================
# 9️⃣ FIND & COUNT
# ========================================

# Q15: Find position of substring

words = "Python is powerful"
print(words.find("powerful"))

# Q16: Count occurrences of a character

text = "banana"
print(text.count("a"))  # 3


# ========================================
# 🔟 STARTSWITH & ENDSWITH
# ========================================

text = "Python"

print(text.startswith("Py"))   # True
print(text.endswith("ono"))    # False


# ========================================
# 1️⃣1️⃣ PALINDROME CHECK
# ========================================

# Q17: Check if a string is palindrome

text = "madam"

if text == text[::-1]:
    print("Palindrome: True")
else:
    print("Palindrome: False")


# ========================================
# 1️⃣2️⃣ COUNT VOWELS
# ========================================

# Q18: Count vowels in string

text = "Anusha"
count = 0

for ch in text.lower():
    if ch in "aeiou":
        count += 1

print("Vowel count:", count)


# ========================================
# 1️⃣3️⃣ REMOVE SPACES
# ========================================

# Q19: Remove spaces from string

text = "Data Science"
print(text.replace(" ", ""))


# ========================================
# 1️⃣4️⃣ CAPITALIZE EACH WORD
# ========================================

# Q20: Capitalize first letter of each word

text = "i love python"
print(text.title())


# ========================================
# 1️⃣5️⃣ MOST FREQUENT CHARACTER
# ========================================

# Q21: Find most frequent character in string

text = "banana"

max_char = ""
max_count = 0

for ch in text:
    count = text.count(ch)
    if count > max_count:
        max_count = count
        max_char = ch

print("Most frequent character:", max_char)

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

git commit -m "Final contribution check"
# contribution after email fix

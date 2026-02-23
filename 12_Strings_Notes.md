Python Strings – Complete Slicing Notes
1️⃣ What is a String?

A string is a sequence of characters enclosed in quotes.

text = "hello"

Strings are:

Ordered

Indexed

Immutable

2️⃣ String Indexing

Each character has a position.

Example:

text = "banana"
b  a  n  a  n  a
0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
Positive Indexing

Starts from 0.

print(text[0])  # b
print(text[3])  # a
Negative Indexing

Starts from -1 (end of string).

print(text[-1])  # a
print(text[-2])  # n
3️⃣ String Slicing

Syntax:

string[start:end:step]

start → included

end → excluded

step → jump value

default step = 1

🔹 Basic Slicing
text = "banana"

print(text[1:4])   # ana
print(text[:3])    # ban
print(text[2:])    # nana
🔹 End is Always Excluded
text = "banana"
print(text[2:5])

Indexes taken:

2 → n
3 → a
4 → n

Output:

nan

Index 5 is NOT included.

4️⃣ Negative Slicing
text = "banana"
print(text[-3:])   # ana
print(text[:-2])   # bana
Rule:

Negative indexes are converted internally to positive.

Example:

text[-3:]  →  text[3:]
5️⃣ Step in Slicing
Step = 2
text = "banana"
print(text[::2])

Take every 2nd character:

Indexes:

0 → b
2 → n
4 → n

Output:

bnn
6️⃣ Reverse a String
text = "banana"
print(text[::-1])

Output:

ananab

Explanation:

Start from end

Move backward

Step = -1

7️⃣ Negative Step (Backward Slicing)

When step is negative:

Start must be greater than end

Movement is right → left

End is still excluded

Example:

text = "abcdefgh"
print(text[6:2:-1])

Indexes:

6 → g
5 → f
4 → e
3 → d

Stop before 2

Output:

gfed
8️⃣ Important Backward Rule

For:

text[6:1:-2]

Move backward by 2:

6 → g
4 → e
2 → c
0 → a

Output:

geca

You stop when you reach or cross the end boundary.

9️⃣ No Wrapping Around

Strings are NOT circular.

Example:

text = "banana"
print(text[-3:])

It will NOT include "b".

Because slicing moves forward by default.

It does NOT wrap to beginning.

🔟 Key Rules Summary
✔ Start Included
✔ End Excluded
✔ Default step = 1
✔ Negative step moves backward
✔ No circular slicing
✔ Negative indexes are converted to positive
1️⃣1️⃣ Common Patterns
First n characters
text[:n]
Last n characters
text[-n:]
Remove last n characters
text[:-n]
Reverse string
text[::-1]
Every 2nd character
text[::2]
1️⃣2️⃣ Complexity

Slicing creates a new string.

Time Complexity → O(n)
Space Complexity → O(n)

Because strings are immutable.

1️⃣3️⃣ Immutability Concept

You cannot change characters directly.

❌

text = "banana"
text[0] = "B"   # ERROR

✔ Correct way:

text = "banana"
new_text = "B" + text[1:]

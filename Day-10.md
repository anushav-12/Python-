Python – Print Statement Notes
1️⃣ What is the print() Statement?

The print() function is used to display output on the screen.

It can print:

Text (strings)

Numbers

Variables

Multiple values together

------------------------------------------------------------------------------------------------
2️⃣ Printing Multiple Parameters

We can pass multiple values inside the print() function separated by commas.

✅ Example 1: Printing Text and Number
print("My name is", "Anusha")
print("My age is", 22)

Output:
My name is Anusha
My age is 22


✅ Example 2: Mixing Text, Numbers, and Variables
name = "Anusha"
age = 22
marks = 95.5

print("Name:", name, "Age:", age, "Marks:", marks)

Output:
Name: Anusha Age: 22 Marks: 95.5


✔ By default, print() adds a space between multiple values.

------------------------------------------------------------------------------------------------
3️⃣ The sep Parameter (Separator)

The sep parameter is used to change the separator between multiple values.

🔹 Default Separator

By default, separator = space " ".

✅ Example 1: Using Dash as Separator
print("2026", "02", "18", sep="-")

Output:
2026-02-18

✅ Example 2: Using Star as Separator
print("Python", "is", "fun", sep="*")

Output:
Python*is*fun

------------------------------------------------------------------------------------------------
4️⃣ The end Parameter

The end parameter controls what is printed at the end of the statement.

🔹 Default Value

By default, end="\n"
(This means it moves to a new line after printing.)

✅ Example 1: Default Behavior (New Line)
print("Hello")
print("World")

Output
Hello
World

Because the default end is \n (new line).

✅ Example 2: Changing end
print("Hello", end=" ")
print("World")

Output:
Hello World

Here, instead of moving to a new line, it prints a space.


✅ Example 3: Using Custom Ending
print("Python", end="!")
print("Programming")

Output:
Python!Programming

------------------------------------------------------------------------------------------------
5️⃣ Using Both sep and end Together
print("2026", "02", "18", sep="-", end=".\n")
print("Done")


Output:
2026-02-18.
Done

--> Summary

-- print() displays output.
-- We can pass multiple values separated by commas.
-- sep changes the separator between values.
-- end changes what appears at the end of the print statement.

Default:
sep = " " (space)
end = "\n" (new line)

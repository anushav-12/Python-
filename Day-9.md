1️⃣ Escape Sequence Characters

Escape sequence characters are special characters used inside strings with a backslash \.
They help us format text in a special way.

🔹 1. \n – New Line

Moves the text to the next line.

print("I love Python\nIt is easy to learn.")

Output:
I love Python
It is easy to learn.

------------------------------------------------------------------------------------------------
🔹 2. \t – Tab Space

Adds a tab space between words.

print("Name:\tAnusha")

Output:
Name:   Anusha

------------------------------------------------------------------------------------------------
🔹 3. \\ – Backslash

Prints a single backslash.

print("This is a backslash: \\")

Output:
This is a backslash: \

------------------------------------------------------------------------------------------------
🔹 4. \' – Single Quote

Prints a single quote inside a string.

print('It\'s a beautiful day.')

Output:
It's a beautiful day.

------------------------------------------------------------------------------------------------
🔹 5. \" – Double Quote

Prints double quotes inside a string.

print("She said, \"Python is fun!\"")

Output:
She said, "Python is fun!"

-------------------------------------------------------------------------------------------------
2️⃣ Comments in Python
------------------------------------------------------------------------------------------------

Comments are used to explain the code.
They are ignored by the Python interpreter.

🔹 Single-Line Comment

Single-line comments start with the hash symbol #.

# This is a single-line comment
print("Hello World")  # This prints Hello World

✔ Used for short explanations.

------------------------------------------------------------------------------------------------
🔹 Multi-Line Comment

Python does not have a special symbol only for multi-line comments, but we use:

✅ Method 1: Multiple #
# This is a multi-line comment
# explaining more than one line
# in Python.

✅ Method 2: Triple Quotes (''' or """)
"""
This is a multi-line comment.
It can span multiple lines.
Used mainly for documentation.
"""

✔ Triple quotes are technically multi-line strings, but commonly used as comments.

------------------------------------------------------------------------------------------------
3️⃣ Shortcut for Commenting Multiple Lines

In most code editors (VS Code, PyCharm, etc.):

👉 Select multiple lines
👉 Press Ctrl + /

This will automatically comment or uncomment all selected lines.

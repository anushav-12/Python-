Python Basics – Modules & pip Notes
📌 What is a Module?

A module is a file that contains Python code (functions, variables, classes) that can be reused in other programs.

Instead of writing everything in one file, we divide code into modules.

Example:
# math_operations.py

def add(a, b):
    return a + b


Now use it in another file:

import math_operations

print(math_operations.add(2, 3))

📌 Types of Modules
1️⃣ Built-in Modules

Already available in Python.

Examples:

math

random

datetime

os

Example:

import math
print(math.sqrt(16))

2️⃣ User-defined Modules

Modules created by us.

3️⃣ External Modules (Third-party)

Modules created by other developers.
We install them using pip.

Examples:

numpy

pandas

flask

requests

📌 What is pip?

pip stands for:

Pip Installs Packages

It is a package manager used to install external Python libraries.

📌 Why Do We Need pip?

Python does not include all libraries by default.

So if we need something advanced (like data science tools), we install it using pip.

📌 Basic pip Commands
Install a package
pip install package_name


Example:

pip install numpy

Check installed packages
pip list

Uninstall a package
pip uninstall package_name

Check pip version
pip --version

📌 How Python Finds Modules

When we write:

import module_name


Python searches:

Current folder

Built-in modules

Installed packages folder

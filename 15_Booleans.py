Python Booleans – Notes

🔹 1. Boolean Data Type

Python Boolean type: bool

Only two values:

True

False

Case-sensitive (must start with capital letter)

x = True
y = False
print(type(x))  # <class 'bool'>

-------------------------------------
🔹 2. Boolean from Comparison Operators

Comparison operators return Boolean values.

Operator	Meaning
==	Equal to
!=	Not equal to
>	Greater than
<	Less than
>=	Greater than or equal
<=	Less than or equal
10 > 5     # True
5 == 3     # False
7 != 2     # True

-------------------------------------
🔹 3. Boolean in Conditional Statements

Booleans are mainly used in decision making.

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

-------------------------------------
🔹 4. Logical Operators
✅ and

Returns True if both conditions are True.

True and True   # True
True and False  # False
✅ or

Returns True if at least one condition is True.

True or False   # True
False or False  # False
✅ not

Reverses the Boolean value.

not True   # False
not False  # True

-------------------------------------
🔹 5. Truthy and Falsy Values
❌ Falsy Values:

0

None

"" (empty string)

[] (empty list)

{}

()

✅ Truthy Values:

Non-zero numbers

Non-empty strings

Non-empty collections

bool(0)      # False
bool(10)     # True
bool("")     # False
bool("Hi")   # True

-------------------------------------
🔹 6. Boolean Conversion

Use bool() function:

bool(1)        # True

bool(0)        # False

bool([])       # False

bool([1,2])    # True

-------------------------------------
🔹 7. Practical Example (Data Perspective)
dlr_status = 30

is_active = dlr_status in [30, 35]

print(is_active)  # True

is_payment_done = True

if is_payment_done:
    print("Include in report")


🧠 Key Points

Boolean type = bool

Values = True, False

Used in conditions & logical operations

Many values automatically evaluate as True or False

Important for filtering data and writing clean logic

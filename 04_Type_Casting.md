Python Type Casting (Type Conversion) 

1️⃣ What is Type Casting?

Type Casting (Type Conversion) means converting one data type into another data type.

Example:

a = "10"   # string

b = 5      # int

print(int(a) + b)

Output:
15

We converted "10" → 10 using int().

----------------------------------------------------------------------------------------

2️⃣ Why Type Casting is Important?

Python does NOT allow operations between incompatible data types.

Example:

a = "10"

b = 5

print(a + b)   # ❌ Error

Because:

"10" → string
 5 → integer

Solution:
print(int(a) + b)  # ✅

----------------------------------------------------------------------------------------
3️⃣ Types of Type Casting

There are 2 types:

🔹 1. Implicit Casting (Automatic)

Python automatically converts one type to another when it is safe.

Rule:

Python only performs implicit casting when:

No data is lost
Conversion is safe
It is a widening conversion

✅ Example: 

int → float

a = 5       # int

b = 2.5     # float

c = a + b

print(c)

print(type(c))

Output:
7.5
<class 'float'>

Python internally converts:

5 → 5.0

Why allowed?
Because no precision is lost.

❌ float → int (Not implicit)

a = 5.8

b = 2

print(a + b)

Python converts:

2 → 2.0

NOT:

5.8 → 5

Why?

Because converting 5.8 → 5 loses .8

Python never performs narrowing conversion automatically.

🔹 Numeric Hierarchy Rule

Python promotes types upward:

int → float → complex

This is called Type Promotion.

Python always moves UP, never DOWN.
----------------------------------------------------------------------------------------
4️⃣ Explicit Casting (Manual)

When we manually convert data types using functions.

🔹 int()

Converts to integer.

a = "100"

b = 10.8

print(int(a))   # 100

print(int(b))   # 10

⚠ Note:

Decimal part is removed (not rounded)

int("10.5") ❌ Error

🔹 float()

Converts to float.

a = "10"

b = 5

print(float(a))  # 10.0

print(float(b))  # 5.0
🔹 str()

Converts anything to string.

a = 100

print(str(a))  # "100"

Useful in concatenation:

age = 22

print("My age is " + str(age))
🔹 bool()

Converts to Boolean.

Rules:

Value	Boolean Result

0	False

0.0	False

""	False

None	False

Everything else	True


Example:

print(bool(0))       # False

print(bool(10))      # True

print(bool(""))      # False

print(bool("Hi"))    # True


🔹 complex()

print(complex(5))      # (5+0j)

print(complex(2,3))    # (2+3j)

----------------------------------------------------------------------------------------

5️⃣ Important Concept: Widening vs Narrowing

🔹 Widening Conversion (Safe)

Automatic

int → float

float → complex

No data loss.

🔹 Narrowing Conversion (Unsafe)

Manual only

float → int

complex → float

May lose precision.

Python forces you to write explicitly:

int(5.8)
----------------------------------------------------------------------------------------
6️⃣ Division Behavior

Even if both numbers are int:

a = 10

b = 2

print(a / b)

print(type(a / b))

Output:

5.0
<class 'float'>

/ always returns float.
----------------------------------------------------------------------------------------
7️⃣ input() Always Returns String

a = input("Enter number: ")

b = input("Enter number: ")

print(a + b)

Input:

5

5

Output:

55

Because input() returns STRING.

Correct way:

a = int(input("Enter number: "))

b = int(input("Enter number: "))

print(a + b)

Output:

10
----------------------------------------------------------------------------------------
8️⃣ Checking Data Type

Use:

type(variable)

Example:

a = "10"

print(type(a))

a = int(a)

print(type(a))
----------------------------------------------------------------------------------------
9️⃣ Key Takeaways

✔ Type Casting = Changing data type

✔ Two types: Implicit & Explicit

✔ Python promotes types upward only

✔ No automatic data loss

✔ int → float is allowed

✔ float → int must be manual

✔ input() always returns string


Python performs implicit casting only when the conversion is safe and does not cause data loss. Narrowing conversions must be done explicitly.

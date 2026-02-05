1. Built-in Data Types
Text Type

str → Stores text

x = "Hello"

Numeric Types

int → Whole numbers

float → Decimal numbers

complex → Complex numbers (a + bj)

x = 10        # int
y = 10.5      # float
z = 1j        # complex

Sequence Types

list → Ordered, mutable

tuple → Ordered, immutable

range → Sequence of numbers

x = [1, 2, 3]
x = (1, 2, 3)
x = range(5)

Mapping Type

dict → Key–value pairs

x = {"name": "Anusha", "age": 22}

Set Types

set → Unordered, unique values

frozenset → Immutable set

x = {"apple", "banana"}
x = frozenset({"apple", "banana"})

Boolean Type

bool → True / False

x = True

Binary Types

bytes → Immutable binary data

bytearray → Mutable binary data

memoryview → Memory access

x = b"Hello"
x = bytearray(5)
x = memoryview(bytes(5))

None Type

NoneType → Represents no value

x = None

2. Getting the Data Type

Use type() to check the data type:

x = 5
print(type(x))   # <class 'int'>

3. Setting Data Type Using Constructors
x = str("Hello")
x = int(20)
x = float(20.5)
x = list(("a", "b", "c"))
x = dict(name="John", age=36)
x = bool(1)

Key Points to Remember

Python assigns data type automatically

type() helps in debugging

Lists & dictionaries are mutable

Tuples & frozensets are immutable

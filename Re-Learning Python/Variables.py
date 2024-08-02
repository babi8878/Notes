# Variables are containers for storing data values. In Python, 
# you do not need to declare variables before using them or declare their type. 
# Variable names can include letters, numbers, and underscores, 
# but they must start with a letter or an underscore.

# Must start with a letter or underscore (_)
# Can contain letters, numbers, and underscores
# Case-sensitive (e.g., name and Name are different)
# Use meaningful names for clarity


# Variable assignment
x = 5               # Integer
y = 3.14            # Float
name = "Alice"      # String
is_student = True   # Boolean


# Multiple assignment
a, b, c = 1, 2, 3


# Type conversion
x = 3.14
y = int(x)
print(f"Convert float to int: {y}")  # Output: 3

x = 5
y = float(x)
print(f"Convert int to float: {y}")  # Output: 5.0

x = 10
y = str(x)
print(f"Convert int to string: {y}")  # Output: '10'

x = "20"
y = int(x)
print(f"Convert string to int: {y}")  # Output: 20

x = "3.14"
y = float(x)
print(f"Convert string to float: {y}")  # Output: 3.14

x = 0
y = bool(x)
print(f"Convert int to boolean: {y}")  # Output: False


# Checking variable types
x = 10
print(f"x is of type: {type(x)}")  # Output: <class 'int'>

y = 3.14
print(f"y is of type: {type(y)}")  # Output: <class 'float'>

name = "Alice"
print(f"name is of type: {type(name)}")  # Output: <class 'str'>

is_student = True
print(f"is_student is of type: {type(is_student)}")  # Output: <class 'bool'>


# Variable scope
def my_function():
    local_variable = 10
    print(f"Local variable inside function: {local_variable}")

my_function()
# print(local_variable)  # Uncommenting this will raise an error


global_variable = 20

def my_function():
    print(f"Global variable inside function: {global_variable}")

my_function()  # Output: 20


def my_function():
    global global_variable
    global_variable = 30

my_function()
print(f"Global variable after modification: {global_variable}")  # Output: 30


# Constants
PI = 3.14159
GRAVITY = 9.8
print(f"Constant PI: {PI}")
print(f"Constant GRAVITY: {GRAVITY}")


# Data structures
# List
fruits = ["apple", "banana", "cherry"]
print(f"List: {fruits}")


# Tuple
coordinates = (10, 20)
print(f"Tuple: {coordinates}")


# Dictionary
person = {"name": "John", "age": 30, "city": "New York"}
print(f"Dictionary: {person}")


# Set
unique_numbers = {1, 2, 3, 4, 5}
print(f"Set: {unique_numbers}")




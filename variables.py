# Declare variables
name = "Alice"
age = 20
height = 5.6
is_student = True

# Print values and their types
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Student:", is_student, "| Type:", type(is_student))
# Multiple assignment
a, b, c = 10, 20, 30

print("After multiple assignment:")
print("a =", a)
print("b =", b)
print("c =", c)

# Assign the same value to all variables
a = b = c = 100

print("\nAfter assigning the same value:")
print("a =", a)
print("b =", b)
print("c =", c)
# (a) Swapping using a temporary variable

a = 10
b = 20

print("Before swapping (using temporary variable):")
print("a =", a, "b =", b)

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a, "b =", b)

# (b) Swapping using Python's tuple unpacking

a = 10
b = 20

print("\nBefore swapping (using tuple unpacking):")
print("a =", a, "b =", b)

a, b = b, a

print("After swapping:")
print("a =", a, "b =", b)
# Demonstrating dynamic typing in Python

value = 100
print("Value:", value)
print("Type:", type(value))

# Reassign the same variable with a string
value = "Hello, Python!"
print("\nValue:", value)
print("Type:", type(value))
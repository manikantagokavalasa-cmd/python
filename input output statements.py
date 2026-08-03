# Taking input from the user
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Printing the message
print("Hello", name + ", you will turn", age + 1, "next year.")
# Taking two numbers as string input
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Converting strings to numbers
num1 = float(num1)
num2 = float(num2)

# Performing operations
sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

# Printing results
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
# Data
name = "Alice"
marks = 95

# 1. Using comma-separated print()
print("Name:", name, "Marks:", marks)

# 2. Using str.format()
print("Name: {} Marks: {}".format(name, marks))

# 3. Using f-strings
print(f"Name: {name} Marks: {marks}")
# Taking multiple values in a single input line
values = input("Enter numbers separated by spaces: ")

# Splitting the input and converting values to integers
numbers = values.split()
numbers = [int(num) for num in numbers]

# Calculating and printing the sum
total = sum(numbers)

print("Sum:", total)
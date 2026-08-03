# Assignment statement
num = 5

# Conditional (if) statement
if num > 0:
    print("The number is positive.")

# Loop statement (for loop)
for i in range(1, num + 1):
    # Print statement
    print("Count:", i)
    # Using the line continuation character (\)
total1 = 10 + 20 + 30 + \
         40 + 50 + 60

print("Total using line continuation:", total1)

# Using implicit continuation with parentheses ()
total2 = (
    10 + 20 + 30 +
    40 + 50 + 60
)

print("Total using parentheses:", total2)
# Multiple statements in a single line separated by semicolons

a = 5; b = 10; print("Sum =", a + b)
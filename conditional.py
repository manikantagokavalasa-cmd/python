num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
    print("Not a valid triangle")
elif a == b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c

print("The largest number is:", largest)
marks = float(input("Enter the student's marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)
ch = input("Enter a character: ")

if ch.isalpha():
    if ch.lower() in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
elif ch.isdigit():
    print("Digit")
else:
    print("Special symbol")
    year = int(input("Enter year: "))
month = int(input("Enter month (1-12): "))
day = int(input("Enter day: "))

# Determine the number of days in the month
if month == 2:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        max_days = 29
    else:
        max_days = 28
elif month in [4, 6, 9, 11]:
    max_days = 30
elif 1 <= month <= 12:
    max_days = 31
else:
    max_days = 0

if year > 0 and 1 <= month <= 12 and 1 <= day <= max_days:
    print("Valid date")
else:
    print("Invalid date")

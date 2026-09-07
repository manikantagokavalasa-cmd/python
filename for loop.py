num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)
num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial:", factorial)
text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)

num = int(input("Enter a number: "))

if num <= 1:
    print("Not a prime number")
else:
    is_prime = True

    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print("Prime number")
    else:
        print("Not a prime number")

lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

print("Prime numbers:")

for num in range(lower, upper + 1):
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num, end=" ")

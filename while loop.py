N = int(input("Enter N: "))

i = 1

while i <= N:
    print(i)
    i += 1
num = int(input("Enter a number: "))

temp = abs(num)
sum_digits = 0
count = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    count += 1
    temp //= 10

if count > 0:
    average = sum_digits / count
else:
    average = 0

print("Sum of digits:", sum_digits)
print("Average of digits:", average)
num = int(input("Enter an integer: "))

reverse = 0
temp = abs(num)

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num < 0:
    reverse = -reverse

print("Reversed integer:", reverse)
num = int(input("Enter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
N = int(input("Enter the number of terms: "))

a = 0
b = 1
count = 0

while count < N:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

a = 23
b = 6

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
m = int(input("Enter m: "))
n = int(input("Enter n: "))

print(m == n)
print(m != n)
print(m > n)
print(m < n)
print(m >= n)
print(m <= n)
score = 50
print(score)

score += 10
print(score)

score -= 10
print(score)

score *= 10
print(score)

score /= 10
print(score)

score //= 10
print(score)

score %= 10
print(score)

score **= 10
print(score)
percentage = float(input("Enter percentage: "))
attendance = float(input("Enter attendance %: "))

eligible = percentage > 75 and attendance > 90

print("Eligible for scholarship:", eligible)
p = 12
q = 10

print(bin(p), bin(q))
print(p & q)
print(p | q)
print(p ^ q)
print(~p)
print(p << 2)
print(p >> 2)
fruits = ["apple", "banana", "mango", "grape", "kiwi"]

item = input("Enter a fruit: ")

print(item, "is in the list:", item in fruits)
print(item, "is not in the list:", item not in fruits)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)
print(list1 is list2)
print(list1 is list3)
print(id(list1), id(list2), id(list3))
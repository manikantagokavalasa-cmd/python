#creating lists
numbers = [10, 25, 7, 42, 18, 33, 5, 29, 14, 50]

print("List:", numbers)
print("Length:", len(numbers))

#out put
List: [10, 25, 7, 42, 18, 33, 5, 29, 14, 50]
Length: 10


my_list = [10, 3.14, "Hello", True, [1, 2, 3]]

for element in my_list:
    print(element, "->", type(element))
#out put
    10 -> <class 'int'>
3.14 -> <class 'float'>
Hello -> <class 'str'>
True -> <class 'bool'>
[1, 2, 3] -> <class 'list'>

my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)

print(my_list)
#out put
[10, 20, 30, 40, 50]

#accessing list elements
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Papaya", "Guava", "Pineapple"]

print(fruits[0])   # First element
print(fruits[-1])  # Last element
print(fruits[3])   # Element at index 3

#out put
Apple
Pineapple
Orange

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

for index, element in enumerate(numbers):
    print("Index:", index, "Element:", element)
    
#example input:
    10 20 30 40 50

#out put:
    Index: 0 Element: 10
Index: 1 Element: 20
Index: 2 Element: 30
Index: 3 Element: 40
Index: 4 Element: 50

#Slicing Lists
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print("First 3 elements:", numbers[:3])
print("Last 3 elements:", numbers[-3:])
print("Alternate elements:", numbers[::2])

#out put
First 3 elements: [10, 20, 30]
Last 3 elements: [80, 90, 100]
Alternate elements: [10, 30, 50, 70, 90]

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

middle = numbers[4:8]

print("Middle 4 elements:", middle)

#out put
Middle 4 elements: [50, 60, 70, 80]

numbers = [10, 20, 30, 40, 50, 60, 70]
#Negative Indices

print("Last element:", numbers[-1])
print("Second-last element:", numbers[-2])
print("Last 3 elements:", numbers[-3:])

#out put
Last element: 70
Second-last element: 60
Last 3 elements: [50, 60, 70]

numbers = [10, 20, 30, 40, 50, 60, 70]

print("Reverse order:", numbers[::-1])

#out put
Reverse order: [70, 60, 50, 40, 30, 20, 10]

#List Methods

numbers = [30, 10, 20, 40, 20]

print("Original list:", numbers)

numbers.append(50)
print("After append():", numbers)

numbers.insert(1, 15)
print("After insert():", numbers)

numbers.extend([60, 70])
print("After extend():", numbers)

numbers.remove(20)
print("After remove():", numbers)

numbers.pop()
print("After pop():", numbers)

numbers.sort()
print("After sort():", numbers)

numbers.reverse()
print("After reverse():", numbers)

print("Count of 20:", numbers.count(20))
print("List after count():", numbers)

print("Index of 40:", numbers.index(40))
print("List after index():", numbers)
#out put
Original list: [30, 10, 20, 40, 20]
After append(): [30, 10, 20, 40, 20, 50]
After insert(): [30, 15, 10, 20, 40, 20, 50]
After extend(): [30, 15, 10, 20, 40, 20, 50, 60, 70]
After remove(): [30, 15, 10, 40, 20, 50, 60, 70]
After pop(): [30, 15, 10, 40, 20, 50, 60, 70]
After sort(): [10, 15, 20, 30, 40, 50, 60, 70]
After reverse(): [70, 60, 50, 40, 30, 20, 15, 10]
Count of 20: 1
List after count(): [70, 60, 50, 40, 30, 20, 15, 10]
Index of 40: 3
List after index(): [70, 60, 50, 40, 30, 20, 15, 10]

numbers = [10, 20, 10, 30, 20, 40, 30, 50]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Original list:", numbers)
print("List without duplicates:", unique_numbers)
#out put
Original list: [10, 20, 10, 30, 20, 40, 30, 50]
List without duplicates: [10, 20, 30, 40, 50]

numbers = [10, 25, 5, 40, 15]

# Find maximum
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

# Find minimum
minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num

# Find sum
total = 0
for num in numbers:
    total += num

print("List:", numbers)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)
#out put
List: [10, 25, 5, 40, 15]
Maximum: 40
Minimum: 5
Sum: 95

list1 = [10, 30, 20, 50]
list2 = [40, 60, 15, 25]

# Merge the two lists
combined = list1 + list2

# Sort in descending order
combined.sort(reverse=True)

print("Merged and sorted list:", combined)
#out put
Merged and sorted list: [60, 50, 40, 30, 25, 20, 15, 10]

#List Comprehensions
squares = [n ** 2 for n in range(1, 21)]

print("Squares:", squares)
#out put
Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

even_numbers = [n for n in range(1, 51) if n % 2 == 0]

print("Even numbers:", even_numbers)
#out put
Even numbers: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

words = ["apple", "cat", "banana", "dog", "elephant", "book", "computer"]

long_words = [word for word in words if len(word) > 4]

print("Words with more than 4 letters:", long_words)
#out put
Words with more than 4 letters: ['apple', 'banana', 'elephant', 'computer']

matrix = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]

#0ut put:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

numbers = [3, -1, 7, -5, 2]

result = [x if x >= 0 else 0 for x in numbers]

print(result)

#out put:

[3, 0, 7, 0, 2]

#creating tuples
countries = ("India", "Japan", "Canada", "Brazil", "Germany", "Australia")

print(countries)
print(type(countries))
print(len(countries))
#out put:
('India', 'Japan', 'Canada', 'Brazil', 'Germany', 'Australia')
<class 'tuple'>
6

my_tuple = ("India",)

print(my_tuple)
print(type(my_tuple))
#0ut put:
('India',)
<class 'tuple'>
#output:
('India',)
<class 'tuple'>

# Convert a list into a tuple
my_list = [10, 20, 30, 40]
my_tuple = tuple(my_list)

# Convert a tuple into a list
another_tuple = (50, 60, 70, 80)
another_list = list(another_tuple)

print("List to Tuple:", my_tuple)
print("Tuple to List:", another_list)
#output:
List to Tuple: (10, 20, 30, 40)
Tuple to List: [50, 60, 70, 80]

# Indexing and Slicing Tuples
# Tuple with 10 elements
my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)

# Print elements using positive and negative indexing
print("Element at index 0:", my_tuple[0])
print("Element at index 5:", my_tuple[5])
print("Last element:", my_tuple[-1])

#output:
Element at index 0: 10
Element at index 5: 60
Last element: 100

# Tuple with 12 elements
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

# Print the first half
print("First half:", my_tuple[:6])

# Print the second half
print("Second half:", my_tuple[6:])
#output:
First half: (1, 2, 3, 4, 5, 6)
Second half: (7, 8, 9, 10, 11, 12)

# Create a tuple
my_tuple = (10, 20, 30, 40, 50)

# Value to search
value = 30

# Check whether the value exists in the tuple
if value in my_tuple:
    print("Value exists in the tuple")
else:
    print("Value does not exist in the tuple")
#output:
Value exists in the tuple

# Create a tuple of numbers
my_tuple = (10, 20, 30, 20, 40, 20, 50)

# Find maximum and minimum values
print("Maximum value:", max(my_tuple))
print("Minimum value:", min(my_tuple))

# Count how many times a given value occurs
value = 20
print("Count of", value, ":", my_tuple.count(value))
#output:
Maximum value: 50
Minimum value: 10
Count of 20 : 3

#Operations on Tuples

# Create two tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenate two tuples using +
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)

# Repeat a tuple 3 times using *
repeated_tuple = tuple1 * 3
print("Repeated tuple:", repeated_tuple)
#output:
Concatenated tuple: (1, 2, 3, 4, 5, 6)
Repeated tuple: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Tuple containing 5 student marks
marks = (80, 75, 90, 85, 70)

# Unpack the tuple into 5 variables
mark1, mark2, mark3, mark4, mark5 = marks

# Calculate the average
average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5

print("Marks:", mark1, mark2, mark3, mark4, mark5)
print("Average:", average)
#output:
Marks: 80 75 90 85 70
Average: 80.0

# Create a tuple
my_tuple = (10, 20, 30)

try:
    # Attempt to modify an element
    my_tuple[0] = 100
except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable and cannot be modified.")
#output:
Error: 'tuple' object does not support item assignment
Tuples are immutable and cannot be modified.

# Tuple containing a nested list
my_tuple = (10, 20, [30, 40], 50)

# Modify the nested list
my_tuple[2][0] = 100

print(my_tuple)

# This is possible because the tuple itself is immutable,
# but the list inside the tuple is mutable and its elements can be changed.
#output:
(10, 20, [100, 40], 50)

# Create a tuple
my_tuple = (50, 20, 40, 10, 30)

# Sort the tuple and store the result as a list
sorted_list = sorted(my_tuple)

print("Original tuple:", my_tuple)
print("Sorted list:", sorted_list)
#output:
Original tuple: (50, 20, 40, 10, 30)
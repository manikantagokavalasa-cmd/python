import keyword

# Print the total number of keywords
print("Total number of keywords:", len(keyword.kwlist))

# Print the full list of keywords
print("\nPython Keywords:")
for kw in keyword.kwlist:
    print(kw)
    import keyword

# Get input from the user
word = input("Enter a word: ")

# Check if the word is a Python keyword
if keyword.iskeyword(word):
    print(word, "is a Python keyword.")
else:
    print(word, "is not a Python keyword.")
    # Demonstrating Python's case sensitivity

Marks = 95
marks = 80

print("Marks =", Marks)
print("marks =", marks)
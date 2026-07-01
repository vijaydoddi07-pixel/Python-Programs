str1 = input("Enter a String: ")

# Reverse
print("Reverse :", str1[::-1])

# Count Vowels
vowels = 0
for ch in str1.lower():
    if ch in "aeiou":
        vowels += 1
print("Vowels :", vowels)

# Count Consonants
consonants = 0
for ch in str1.lower():
    if ch.isalpha() and ch not in "aeiou":
        consonants += 1
print("Consonants :", consonants)

# Palindrome
if str1 == str1[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Remove Spaces
print("Without Spaces :", str1.replace(" ", ""))

# Uppercase and Lowercase
print("Uppercase :", str1.upper())
print("Lowercase :", str1.lower())

# Count Words
words = str1.split()
print("Total Words :", len(words))

# Duplicate Characters
print("Duplicate Characters:")
for ch in set(str1):
    if ch != " " and str1.count(ch) > 1:
        print(ch)

# Frequency of Each Character
print("Character Frequency:")
for ch in set(str1):
    if ch != " ":
        print(ch, "=", str1.count(ch))

# String Slicing
print("First 5 Characters :", str1[:5])
print("Last 5 Characters :", str1[-5:])
print("Reverse using Slicing :", str1[::-1])

# String Methods
print("Title :", str1.title())
print("Capitalize :", str1.capitalize())
print("Swapcase :", str1.swapcase())
print("Length :", len(str1))
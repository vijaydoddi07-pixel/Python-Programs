str1 = input("Enter First String: ")
str2 = input("Enter Second String: ")

# Anagram
if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")

# Replace Character
old = input("Character to Replace: ")
new = input("New Character: ")

print("After Replace :", str1.replace(old, new))

# Split
print("Split :", str1.split())

# Join
list1 = str1.split()
print("Join :", "-".join(list1))
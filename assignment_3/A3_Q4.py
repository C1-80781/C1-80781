#
# 4)Write a program to find index of element ‘e’ in given vowels list [’a’, ’e’, ’i’, ’o’, ’i’, ’u’]
#

vowels = ["a", "e", "i", "o", "i", "u"]

for index in range(len(vowels)):
    if vowels[index] == "e":
        print(f"The index of 'e': {index}")

# 3) Write a program that reads a string from keyboard and display:
# * The number of uppercase letters in the string
# * The number of lowercase letters in the string
# * The number of digits in the string
# * The number of whitespace characters in the string

string = input("Enter the string: ")

list = list(string)

upper_count = 0
lower_count = 0
digit_count = 0
space_count = 0

for i in list:
    if i.isupper():
        upper_count += 1
    elif i.islower():
        lower_count += 1
    elif i.isdigit():
        digit_count += 1
    elif i == " ":
        space_count += 1

print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
print(f"Digits: {digit_count}")
print(f"Spaces: {space_count}")

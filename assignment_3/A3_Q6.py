#
# 6) Find and display the largest number of a list without using built-in function max().
# Your program should ask the user to input values in list from keyboard.

length = int(input("Enter length of list: "))
list = []
max_int = 0

for i in range(length):
    value = int(input("Enter the value: "))
    list.append(value)

    if value > max_int:
        max_int = value

print(f"Largest number of list {list}: {max_int}")

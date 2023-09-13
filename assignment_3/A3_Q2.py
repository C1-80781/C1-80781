#
# 2) Write a program that accepts a list from user and print the alternate element of list.
#
n = int(input("Enter length of list: "))

new_list = []

# 'for loop' to insert values in the list
for index in range(n):
    value = int(input("Enter value: "))
    new_list.append(value)

print(f"The alternate values are: ")
for i in range(0, n, 2):
    print(f"{new_list[i]}")

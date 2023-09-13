#
# 2) Write a Python Program to find the repeated item of a tuple
# (Take a value from user which you want to find)
#

tuple = (10, 20, 40, 10, 50, 70, 20, 10)

user_input = int(input("Enter the value to find: "))

count = tuple.count(user_input)

print(f"The number [{user_input}] is repeated {count} times")





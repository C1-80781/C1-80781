#
# 1)Using for loop, write and run a Python program to find factorial from 0 to 10.
#
factorial = 1
for num in range(11):
    if num == 0:
        print(f"factorial of 0 = 1")
    else:
        factorial *= num
        print(f"factorial of {num} = {factorial}")


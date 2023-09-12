# 1) Write A Program which is taking 5 int value and calculate sum of cube of all numbers [Write cube function]

def calculate_cube():
    cube = 0
    for num in range(5):
        num = int(input("Enter the no. : "))
        cube += num ** 3

    print(f"The sum of cube of above 5 numbers is {cube}")


# function call
calculate_cube()

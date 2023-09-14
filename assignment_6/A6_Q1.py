#
# 1)Write a menu Driven Program To Calculate the Parameter and Area of
# different Shapes(Circle,Square,Rectangle) using functions
#
def perimeter_of_circle():
    r = int(input("Enter radius of circle: "))
    print(f"The perimeter of circle of radius {r} = {2 * 3.14 * r}")

def perimeter_of_square():
    w = int(input("Enter width of square: "))
    print(f"The perimeter of square of width {w} = {4 * w}")

def perimeter_of_rectangle():
    l = int(input("Enter length of rectangle: "))
    w = int(input("Enter width of rectangle: "))
    print(f"The perimeter of rectangle of {l}x{w} = {2 * (l + w)}")

def area_of_circle():
    r = int(input("Enter radius of circle: "))
    print(f"The area of circle of radius {r} = {r * 3.14 * r}")

def area_of_square():
    w = int(input("Enter width of square: "))
    print(f"The area of square of width {w} = {w * w}")

def area_of_rectangle():
    l = int(input("Enter length of rectangle: "))
    w = int(input("Enter width of rectangle: "))
    print(f"The perimeter of rectangle of {l}x{w} = {l * w}")

def print_menu():
    print("-" * 80)
    print("Welcome to the calculator!")
    print("1. primeter of circle")
    print("2. primeter of square")
    print("3. primeter of rectangle")
    print("4. area of circle")
    print("5. area of square")
    print("6. area of rectangle")
    print("0. EXIT")
    print("-" * 80)

while True:
    print_menu()
    user_input = int(input("Enter your response: "))
    if user_input == 1:
        perimeter_of_circle()
    elif user_input == 2:
        perimeter_of_square()
    elif user_input == 3:
        perimeter_of_rectangle()
    elif user_input == 4:
        area_of_circle()
    elif user_input == 5:
        area_of_square()
    elif user_input == 6:
        area_of_rectangle()
    else:
        break

print("Thanks !!!")
print("-" * 80)


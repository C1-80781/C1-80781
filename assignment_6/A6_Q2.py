#
# 2)Display following menu and write required function for it
# A. Display characters from even position
# B. Display characters from odd position
# C. Display length of a string
# D. Add a at the end of string length times
#

def display_from_even(string):
    even_characters = string[1::2]
    print("The characters from even positions are:", even_characters)

def display_from_odd(string):
    odd_characters = string[::2]
    print("Characters from odd positions:", odd_characters)

def display_length_string(string):
    length = len(string)
    print("Length of given string:", length)

def adding_a(string):
    length = len(string)
    str2 = string + 'a' * length
    print("Added a at end of string:", str2)



def print_menu():
    print("*" * 80)
    print("Welcome ! what you want to do....")
    print("A. Display characters from even position      C. Display length of a string")
    print("B. Display characters from odd position       D. Add 'a' at the end of string length times")
    print("E. EXIT")
    print("*" * 80)

while True:
    print_menu()
    user_input = input("Enter the choice: ")
    if user_input == 'A':
        input_string = input("Enter a string: ")
        display_from_even(input_string)
    elif user_input == 'B':
        input_string = input("Enter a string: ")
        display_from_odd(input_string)
    elif user_input == 'C':
        input_string = input("Enter a string: ")
        display_length_string(input_string)
    elif user_input == 'D':
        input_string = input("Enter a string: ")
        adding_a(input_string)
    elif user_input == 'E':
        print("Exiting the program.")
        break
    else:
        print("Invalid input")




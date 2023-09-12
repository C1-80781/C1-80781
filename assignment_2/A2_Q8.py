#
# 8)Write a program that prompts the user to input a character and determine the character is vowel or consonant.

user_input = input("Enter a character: ")

vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

if user_input in vowels:
    print(f"{user_input} is a Vowel")

else:
    print(f"'{user_input}' is NOT a Vowel")

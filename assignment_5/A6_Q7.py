
# 7)Write a program in Python to read a string from the keyboard. Replace each ‘this’ word
# with ‘that word’ in this String. Example: this is me and this is my python program.
# Output: That is me and That is my python program

str1 = str(input("Enter the string: "))

str2 = str1.replace("this", "that")
print(f"Replaced output: {str2}")

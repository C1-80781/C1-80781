
# 2] Write a Python Program to Convert Celsius To Fahrenheit vice versa.

celsius1 = int(input("Enter the celsius: "))
fahrenheit1 = (celsius1 * 1.8) + 32
print(f"Conversion of °F to °C: {celsius1}°C = {fahrenheit1:.2f}°F")

fahrenheit2 = int(input("Enter the fahrenheit: "))
celsius2 = (fahrenheit2 - 32) / 1.8
print(f"Conversion °F to °C: {fahrenheit2}°C is equal to {celsius2:.2f}°F")

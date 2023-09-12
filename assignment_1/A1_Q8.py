
# 8] Write a program that prompts the user to input number of calls and calculate the monthly telephone bills
# as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls.

no_of_calls = int(input("Please enter No. of calls: "))
monthly_bill = 0

if no_of_calls <= 100:
    monthly_bill = 200

elif no_of_calls <= 150:
    monthly_bill = 200 + (no_of_calls - 100) * 0.6

elif no_of_calls <= 200:
    monthly_bill = 200 + ((no_of_calls - 150) * 0.5) + 30

else:
    monthly_bill = 200 + 25 + 30 + ((no_of_calls - 200) * 0.4)

print(f"Monthly telephone bill of {no_of_calls} calls = Rs. {monthly_bill}")

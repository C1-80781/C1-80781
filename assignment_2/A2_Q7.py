#
# 7) Write a program that will calculate the price for a quantity entered from the keyboard, given that the unit
# price is Rs 5 and there is a discount of 10 percent for quantities over 30 and a 15 percent discount for qu
# antities over 50.
#

quantity = int(input("Enter quantity: "))

price = 0

if quantity >= 50:
    total = 5 * quantity
    price = total - (total / 0.15)

elif quantity >= 30:
    total = 5 * quantity
    price = total - (total / 10)

else:
    price = quantity * 5

print(f"The price of given quantity: {price}")

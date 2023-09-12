
# 6] Write a Python Program Get age input from user and check if user is eligible for voting

age_input = int(input("Please enter your Age: "))

can_vote = False

if age_input <= 17:
    print("No! User is  not eligible for VOTE!!")
else:
    can_vote = True
    print("Yes! User is eligible for VOTE")


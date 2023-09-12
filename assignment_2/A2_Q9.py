
# 9) write a function to return simple interest

def calculate_simple_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest


p = int(input("Enter principal: "))
r = int(input("Enter rate of amount: "))
t = int(input("Enter time in year: "))

print(f"Simple interest is: {calculate_simple_interest(p, r, t)}")



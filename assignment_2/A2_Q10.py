# 10) write a function to return compound interest

def calculate_compound_interest(principal, rate, time):
    simple_interest = principal * ((1 + (rate / 100)) ** time) - principal
    return simple_interest


print(f"Compound interest is: {calculate_compound_interest(200000, 9.5, 10)}")

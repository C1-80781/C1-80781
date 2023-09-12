# 3] Write a program to accept a 4 digit number and
# a. Display face value of each decimal digit
# b. Display place value of each decimal digit
# c. Display no in reverse order by changing decimal place values If user enters a 4-digit number

number = int(input("Enter 4 digit number: "))

_1st_digit = number // 1000
_2nd_digit = (number // 100) - (_1st_digit * 10)
_3rd_digit = (number % 100) // 10
_4th_digit = number % 10

# first case
print(_1st_digit, _2nd_digit, _3rd_digit, _4th_digit)

# second case
print(f"{number} = {_1st_digit * 1000} + {_2nd_digit * 100} + {_3rd_digit * 10} + {_4th_digit}")

# third case
print(f"{_4th_digit * 1000 + _3rd_digit * 100 + _2nd_digit * 10 + _1st_digit}")



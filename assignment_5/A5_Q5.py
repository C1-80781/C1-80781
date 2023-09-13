# 5)Write a program to read 6 numbers and create a dictionary having keys EVEN and ODD.
# Dictionary's value should be stored in list. Your dictionary should be like:
# {'EVEN':[8,10,64], 'ODD':[1,5,9]}

A = {}
Even = []
Odd = []
i = 1
for i in range(6):
    num = int(input("Enter number: "))
    if (num % 2 == 0):
        Even.append(num);
    else:
        Odd.append(num);

A['EVEN'] = Even
A['ODD'] = Odd
print(A)

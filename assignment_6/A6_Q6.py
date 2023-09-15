#
# 6)Write a program that rotates the element of a list so that the element at the
# first index moves to the second index, the element in the second index moves to
# the third index, etc., and the element in the last index moves to the first index.Input:- [‘Sunday’,’Monday’,’Tuesday’,’Wednesday’]
# Output:- [’Wednesday’, ‘Sunday’, ’Monday’, ’Tuesday’]
#


c_num = int(input("Enter the count of string: "))
list_1 = []
name = ""

for i in range(c_num):
    name = input("Enter the week: ")
    list_1.append(name)
print(list_1)

list_2 = []

for j in range(0, len(list_1) - 1):
    val = list_1[j]
    list_2.append(val)
print(list_2)



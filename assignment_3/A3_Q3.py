#
# 3)Replace single element ‘b’ in given list [’a’, ’b’, ’c’, ’d’, ’e’] with [1, 2, 3]
#
list = ['a', 'b', 'c', 'd', 'e']

for index in range(len(list)):
    if list[index] == 'b':
        list[index] = [1, 2, 3]

print(list)

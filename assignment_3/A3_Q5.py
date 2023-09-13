#
# 5)Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
# False otherwise.
#
def overlapping(list1, list2):
    for i in list1:
        for j in list2:
            if j == i:
                return True
    return False


list1 = [1, 2, 33, 4, 5]
list2 = [3, 22, 3, 41, 35]

print(overlapping(list1, list2))

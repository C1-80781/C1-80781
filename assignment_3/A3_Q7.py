#
# 7) Write a function filter_long_words() that takes a list of words and an integer
# len and returns the list of words that are longer than len.
#

def filter_long_words(list, len):
    list1 = []
    for i in list:
        k = 0
        for j in i:
            k += 1
        if k > len:
            list1.append(i)
            print(i)
    return list1


list = ["asif", "ab3sg", "abfdc", "c3d"]

print(filter_long_words(list, 3))
print(filter_long_words(list, 4))

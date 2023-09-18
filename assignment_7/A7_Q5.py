#
# 5)Write a Python program to count the number of characters (character
# frequency) in a string. Go to the editor
# Input:-
# Sample String : sunbeaminfo.com
# Output:-
# {'s': 1, 'u': 1, 'n': 2, 'b': 1, 'e': 1, 'a': 1, 'm': 2, 'i': 1, 'f': 1, 'o': 2, '.': 1, 'c': 1}
#


def counter(str1):
    l1 = list(str1)
    d1 = {}

    for i in l1:
        if d1.get(i) is None:
            d1[i] = 1
        else:
            d1[i] += 1
    print(d1)

str1 = input("Enter string: ")
counter(str1)


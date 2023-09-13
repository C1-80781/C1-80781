#
# 5) Write a function find_longest_word() that takes a list of words and returns
# the length of the longest one.
#

def find_longest_word(list):
    max = 0
    for i in list:
        if len(i) > max:
            max = len(i)
    return max


list = ["dinesh", "sar", "sadh", "hae"]
length_of_longest_one = find_longest_word(list)

print(f"Length of longest word in list: {length_of_longest_one}")

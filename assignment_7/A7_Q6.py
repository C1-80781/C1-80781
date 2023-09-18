#
#
# 6) A pangram is a sentence that contains all the letters of the English alphabet at
# least once,
# for example: The quick brown fox jumps over the lazy dog. Your task here is to
# write a
# function to check a sentence to see if it is a pangram or not.
#

def is_pangram(s):
    l1 = list(s.lower())

    str2 = "thequickbrownfoxjumpsoverthelazydog"
    l2 = list(str2)

    is_pangram = True

    for i in range(len(l2)):
        if l2[i] not in l1:
            print("The Sentence is NOT a pangram!")
            is_pangram = False
            break
    if is_pangram:
        print("The Sentence is a pangram!")


s = input("enter sentence: ")
is_pangram(s)

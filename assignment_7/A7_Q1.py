#
#
# 1) Write a version of a palindrome recognizer that also accepts phrase
# palindromes such as "Go hanga salami I'm a lasagna hog.", "Was it a rat I
# saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no
# basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a
# tired nude Maori","Rise to vote sir", or the exclamation "Dammit, I'm mad!".
# Note that
# punctuation, capitalization, and spacing are usually ignored.
#

user_input = input("Enter phrase: ")
a1 = list(user_input.lower())

l1 = []

for i in range(len(a1)):
    if a1[i] not in [' ', '!', ',', "'", '.']:
        l1.append(a1[i])

str1 = ''.join(l1)

if str1 == str1[::-1]:
    print("Its a Palindrome!")
else:
    print("Its NOT a Palindrome!")



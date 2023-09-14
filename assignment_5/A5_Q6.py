

# 6) Write a function translate() that will translate a text into "rövarspråket"
# (Swedish for "robber's language"). That is, double every consonant and place an
# occurrence of "o" in between. For example, translate("this is fun") should return
# the string "tothohisos isos fofunon".

def translate():

    input_ = input("Enter the string: ")
    list_ = list(input_)
    str = []

    for i in range(len(list_)):
        if list_[i] == ' ' or list_[i] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            str.append(list_[i])

        else:
            str.append(list_[i] + 'o' + list_[i])
    print(''.join(str))


translate()

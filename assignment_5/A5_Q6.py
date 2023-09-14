

# 6) Write a function translate() that will translate a text into "rövarspråket"
# (Swedish for "robber's language"). That is, double every consonant and place an
# occurrence of "o" in between. For example, translate("this is fun") should return
# the string "tothohisos isos fofunon".

def translate():

    string = input("Enter the string: ")
    l1 = list(string)
    list1 = []
    str2 = []

    for i in l1:
        if i == ['a', 'e', 'i', 'u', 'o']:
            i.append(list1)
        else:
            str2.append(i)
            str2.append("o")
            str2.append(i)

    print(''.join(str2))

translate()

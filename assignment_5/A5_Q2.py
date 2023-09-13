# 2) Write a program to sum all the values of a dictionary.
# Hint dict1 = {‘key 1’: 200, ‘key 2’: 300}

dict1 = {'key1': 200,'key2': 300};

sum = 0
for i in dict1:
    sum = sum + dict1[i]

print(f"Sum of all values of dictionary: {sum}");


# 1) Given a dictionary of students and their favourite colours:
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}
# A. Find out how many students are in the list
# B. Change Lisa’s favourite colour
# C. Remove 'Jenny' and her favourite colour
# D. Sort and print students and their favourite colours alphabetically by name

people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink', };
# A. Find out how many students are in the list
sum = 0
for i in people:
    sum = sum + 1
print(sum)

# B. Change Lisa’s favourite colour
people["Lisa"] = "Red";
for i in people:
    print(i, people[i]);
print("\n");

# D. Sort and print students and their favourite colours alphabetically by name
sorted_dict = dict(sorted(people.items()))
print(sorted_dict);
print("\n");

# C. Remove 'Jenny' and her favourite colour
del people["Jenny"]
for i in people:
    print(i, people[i]);

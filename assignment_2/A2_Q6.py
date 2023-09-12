#
# 6)The marks obtained by a student in 3 different subjects are input by the user. Your program should calculate the average of subjects and display the grade. The student gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F

mark1 = int(input("Enter marks: "))
mark2 = int(input("Enter marks: "))
mark3 = int(input("Enter marks: "))

average = (mark1 + mark2 + mark3) / 3

if 90 <= average <= 100:
    print(f"The grade: A")

elif 80 <= average <= 89:
    print(f"The grade: B")

elif 70 <= average <= 79:
    print(f"The grade: C")

elif 60 <= average <= 69:
    print(f"The grade: D")

elif 0 <= average <= 59:
    print(f"The grade: F")

else:
    print("Please enter valid marks!")


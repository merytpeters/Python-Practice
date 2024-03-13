#!/usr/bin/python3
age = eval(input("Enter age: "))
if (age < 5):
    print("Too young for school")
elif age == 5:
    print("Go to Kindergarten")
elif (age >= 6) and (age <= 17):
    grade = age - 5
    print("Go to grade {}" .format(grade))
elif (age < 65):
    print("Go to College")
else:
    print("Maybe retire")

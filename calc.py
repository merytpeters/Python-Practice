#!/usr/bin/python3
num1, operator, num2 = input('Enter operands and operator ').split()
num1 = int(num1)
num2 = int(num2)

if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "-":
    print("{} - {} = {}".format(num1, num2, num1-num2))
elif operator == "*":
    print("{} * {} = {}".format(num1, num2, num1*num2))
elif operator == "/":
    print("{} / {} = {}".format(num1, num2, num1/num2))
else:
    print("Not a known operator")

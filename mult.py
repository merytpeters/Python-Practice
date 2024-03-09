#!/usr/bin/python3
def mul(a, b, c):
    return a * b * c

numbers = (input("Enter three numbers: "))
num = numbers.split()
result = mul(int(num[0]), int(num[1]), int(num[2]))
print("Result = ", result)

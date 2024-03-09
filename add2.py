#!/usr/bin/python3
def add(a, b):
    return a + b

num = input("Enter two numbers: ")
numbers = num.split()
result = add(int(numbers[0]), int(numbers[1]))
print(result)

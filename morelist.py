#!/usr/bin/python3
a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
result = list(map(lambda x, y, z : x+y+z, a, b, c))
print(result)
result = list(map(lambda x, y : x+y, a, b))
print(result)
result = list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c))
print(result)

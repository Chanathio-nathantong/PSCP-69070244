""" Ink """
import math

s, num = map(int, input().split())
time = []

for i in range(num):
    i += 1
    x, y = map(int, input().split())
    a = 3.1416 * ((x ** 2) + (y ** 2))
    result = a / s
    result = math.ceil(result)
    time.append(result)
for j in time:
    print(j)

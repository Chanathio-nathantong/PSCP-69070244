""" Divide By 10 """
num = int(input())
for i in range(num, -1, -1):
    cal = i % 10
    if not cal:
        print(i, end=" ")

""" Blick Bird """
a = int(input())
b = int(input())
goal = int(input())

total_b = goal // 5

if total_b >= b:
    used_b = b
else:
    used_b = total_b

goal = goal - (used_b * 5)
total_a = goal

if a >= total_a :
    print(total_a)
else:
    print("-1")

""" Duplicate I """
num1 = int(input())
num2 = int(input())
group1 = []
same = []

for i in range(num1):
    i += 1
    group1.append(int(input()))

for j in range(num2):
    j += 1
    group2 = int(input())
    if group2 in group1:
        same.append(group2)

if not same:
    print("Nope")
else:
    same.sort(reverse=True)
    for n in same:
        print(n)

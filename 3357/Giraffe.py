""" Giraffe """
num = int(input())
high = []
for i in range(num):
    i += 1
    high.append(int(input()))

count = 0

for j in range(num):
    tall_left = (not j) or (high[j] > high[j - 1])
    tall_right = (j == num - 1) or (high [j] > high[j + 1])
    if tall_left and tall_right:
        count += 1

print(count)

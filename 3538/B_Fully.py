""" B - Fully """
s = input().strip()

seen_order = []
counts = {}

for char in s:
    if char not in counts:
        seen_order.append(char)
        counts[char] = 0
    counts[char] += 1

unpaired = []

for char in seen_order:
    if counts[char] % 2:
        unpaired.append(char)

if not unpaired:
    print("fully paired")
else:
    print("".join(unpaired))

""" Surprising """
total = float(input())
highest = float(input())
minimum = max(0, total - 2 * highest)
if highest - minimum > 2.0:
    print("Surprising")
else:
    print("Not surprising")

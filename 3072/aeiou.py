""" A E I O U """
word = input().lower()
dec = ["a", "e", "i", "o", "u"]
count = [0, 0, 0, 0, 0]
for i in word:
    if i in dec:
        dix = dec.index(i)
        count[dix] += 1
for j in range(5):
    if count[j] > 0:
        print(f"{dec[j]} : {count[j]}")

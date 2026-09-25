""" BigFrame """
text1 = input()
text2 = input()
text3 = input()
text4 = input()
text5 = input()

high = max(len(text1), len(text2), len(text3), len(text4), len(text5))
border = "*" * (high + 4)

print(border)
print(f"* {text1.ljust(high)} *")
print(f"* {text2.ljust(high)} *")
print(f"* {text3.ljust(high)} *")
print(f"* {text4.ljust(high)} *")
print(f"* {text5.ljust(high)} *")
print(border)

""" ไพ่ 44 ใบ """
name = input().upper()
FRONT = ""
BACK = ""

if name[:-1] == "2":
    FRONT = "2"
elif name[:-1] == "3":
    FRONT = "3"
elif name[:-1] == "4":
    FRONT = "4"
elif name[:-1] == "5":
    FRONT = "5"
elif name[:-1] == "6":
    FRONT = "6"
elif name[:-1] == "7":
    FRONT = "7"
elif name[:-1] == "8":
    FRONT = "8"
elif name[:-1] == "9":
    FRONT = "9"
elif name[:-1] == "10":
    FRONT = "10"
elif name[:-1] == "A":
    FRONT = "ace"
elif name[:-1] == "J":
    FRONT = "jack"
elif name[:-1] == "Q":
    FRONT = "queen"
elif name[:-1] == "K":
    FRONT = "king"

if name[-1] == "D":
    BACK = "diamonds"
elif name[-1] == "H":
    BACK = "hearts"
elif name[-1] == "S":
    BACK = "spades"
elif name[-1] == "C":
    BACK = "clubs"

print(FRONT, "of", BACK, sep=" ")

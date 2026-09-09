""" สลากกินแบ่ง """
char_win, win = input().split()
char, buy = input().split()

if char == char_win and buy == win:
    print("1000000")
elif char != char_win and buy == win:
    print("100000")
elif char == char_win and buy[2:] == win[2:]:
    print("2000")
elif char == char_win and buy[3:] == win[3:]:
    print("1000")
elif char != char_win and buy[2:] == win[2:]:
    print("200")
elif char != char_win and buy[3:] == win[3:]:
    print("100")
elif char == char_win and buy != win:
    print("20")
else:
    print("0")

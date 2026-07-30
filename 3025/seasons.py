""" saesons """
mon = float(input())
da = float(input())
if mon in (1, 2, 3):
    season = "winter"
    if da >= 21 and mon == 3:
        season = "spring"
elif mon in (4, 5, 6):
    season = "spring"
    if da >= 21 and mon == 6:
        season = "summer"
elif mon in (7, 8, 9):
    season = "summer"
    if da >= 21 and mon == 9:
        season = "fall"
elif mon in (10, 11, 12):
    season = "fall"
    if da >= 21 and mon == 12:
        season = "winter"
else:
    season = "Invalid input"
print(season)

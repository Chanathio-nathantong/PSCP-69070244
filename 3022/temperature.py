""" Temperature """
tem = float(input())
tem_base = input().strip()
tem_final = input().strip()
tem_out = tem
if tem_base == "C":
    if tem_final == "K":
        tem_out = tem + 273.15
    elif tem_final == "F":
        tem_out = ((tem * 9) / 5) + 32
    elif tem_final == "R":
        tem_out = ((tem + 273.15) * 9) / 5
elif tem_base == "K":
    if tem_final == "C":
        tem_out = tem - 273.15
    elif tem_final == "F":
        tem_out = (((tem - 273.15) * 9) / 5) + 32
    elif tem_final == "R":
        tem_out = (((tem - 273.15) +  273.15) * 9) / 5
elif tem_base == "F":
    if tem_final == "C":
        tem_out = ((tem - 32) *  5) / 9
    elif tem_final == "K":
        tem_out = ((tem -32) * 5 / 9) +  273.15
    elif tem_final == "R":
        tem_out = tem + 459.67
elif tem_base == "R":
    if tem_final == "C":
        tem_out = ((tem - 491.67) * 5) / 9
    elif tem_final == "K":
        tem_out = (tem * 5) / 9
    elif tem_final == "F":
        tem_out = tem - 459.67
print(f"{tem_out:.2f}")

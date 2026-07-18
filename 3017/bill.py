""" Bill for calculate """
num = int(input())
VAT = 0.07
service = num * 0.1
if service < 50:
    service = 50
elif service > 1000:
    service = 1000
cost_service = service + num
cost = cost_service * VAT
totol_cost = cost_service + cost
print(f"{totol_cost:.2f}")

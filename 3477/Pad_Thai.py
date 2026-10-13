""" Pad Thai """
def main():
    """ main """
    own = {
        "Pad Thai Sauce", "Tofu", "Pickle Turnip",
        "Shrimp", "Bean Sprouts", "Noodle",
        "Chives", "Lime", "Egg", "Oil", "Peanuts"
        }
    flavor = {"Sweet", "Sour", "Salty"}

    use_own = set()
    use_favor = set()

    while True:
        try:
            line = input()
            if line == "Cook":
                break
            if line:
                use_own.add(line)
        except EOFError:
            break

    while True:
        try:
            line = input()
            if line == "End":
                break
            if line:
                use_favor.add(line)
        except EOFError:
            break

    if not use_own.issubset(own):
        print("This is not Pad Thai!!!")
    elif use_own != own:
        print("This is bad!")
    else:
        if use_favor == flavor:
            print("Delicious!")
        else:
            print("Not Bad...")
main()

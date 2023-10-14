human_age = int(input("What is your age? "))
if human_age == 0:
    print("You are baby!")
elif 1<=human_age<=3:
    print("You are toddler!")
elif 4<=human_age<=7:
    print("You are kid!")
elif 8<=human_age<=11:
    print("You are tween!")
elif 12<=human_age<=17:
    print("You are teenager!")
elif 18<=human_age<=25:
    print("You are young adult!")
elif 25<=human_age<=60:
    print("You are adult!")
elif human_age>60:
    print("You are old guy!")
elif human_age>130:
    print("Damn cheater!")
else:
    print("You are unborn cheater!")
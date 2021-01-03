tm = int(input("Total Match Played = "))
tr = int(input("Total Run Scored = "))
tw = int(input("Total Wicket Taken = "))

if tr > 40:
    if tw >= 3:
        print("You are a AllRounder")
else:
    if tr > 45:
        print("You are a Batsman")
    else:
        if tw >= 4:
            print("You are a Bowler")
        else:
            print("You are a Fielder")
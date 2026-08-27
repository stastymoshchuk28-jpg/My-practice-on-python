#Done
#v1.0

pointstowin = int(input("Enter the number of points needed to win: "))

playerpoints = int(input("Enter the number of points that you have: "))

lifes = 1

ghosts = 5
if playerpoints >= pointstowin:
    if playerpoints >= 10000:
        lifes += 1
        print("You have +1 life!")
        exit = input("Do you want find exit (yes/no)? ").lower()
        if exit == "yes":
            superpower = input("Do you want to use superpower (yes/no)? ").lower()
            if superpower == "yes":
                print("You used superpower! You can eat ghosts!")
                ghosts -= 5
                print(f"You have {ghosts} ghosts left!")
                print("You found the exit! You win!")
            else:
                print("You didn't use superpower. You found the exit! You win!")
        else:
            print("You didn't find the exit. You lose!")
    else:
        print("You didn't get enough points to get an extra life!")
        exit = input("Do you want find exit (yes/no)? ").lower()
        if exit == "yes":
            superpower = input("Do you want to use superpower (yes/no)? ").lower()
            if superpower == "yes":
                print("You used superpower! You can eat ghosts!")
                ghosts -= 5
                print(f"You have {ghosts} ghosts left!")
                print("You found the exit! You win!")
            else:
                print("You didn't use superpower. You found the exit! You win!")
        else:
            print("You didn't find the exit. You lose!")
else:
    print(f"You need {pointstowin - playerpoints} more points to win.")
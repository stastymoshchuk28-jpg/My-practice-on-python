#done!

print("Welcome to the skin buying store!")
print(" ")
skins = ["Dragon knife (Karambit)", "Polar gradient knife (Butterfly)", "Sun knife (Karambit)"]
print("Here are the skins we have in stock:")
print(" ")
print("1. " + skins[0])
print("2. " + skins[1])
print("3. " + skins[2])
print(" ")
choice = int(input("Please enter the number of the skin you would like to buy: "))
print(" ")
money = int(input("Please enter the amount of money you have: "))
print(" ")
if choice == 1:
    if money >= 10000:
        print("Congratulations! You have bought the " + skins[0] + " for $10000!")
        print(" ")
        print("Thank you for your purchase! Enjoy your new skin!")
    else:
        print("Sorry, you do not have enough money to buy the " + skins[0] + ".")
elif choice == 2:
    if money >= 7500:
        print("Congratulations! You have bought the " + skins[1] + " for $7500!")
        print(" ")
        print("Thank you for your purchase! Enjoy your new skin!")
    else:
        print("Sorry, you do not have enough money to buy the " + skins[1] + ".")
elif choice == 3:
    if money >= 5000:
        print("Congratulations! You have bought the " + skins[2] + " for $5000!")
        print(" ")
        print("Thank you for your purchase! Enjoy your new skin!")
    else:
        print("Sorry, you do not have enough money to buy the " + skins[2] + ".")
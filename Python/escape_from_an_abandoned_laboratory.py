#Done
#v1.0

print("Welcome to text minigame: Escape from an Abandoned Laboratory!")
print("-----------------------------------------------")
Name = input("What is your name? ").capitalize()
print(f"Hello {Name}, welcome to the game!")
print("-----------------------------------------------")
print("Story:")
print("You are in an abandoned laboratory.")
print("You wake up in a cold, dark room.")
print("The neon lights are flickering.")
print("You don't remember how you got here.")
print("A computer screen in front of you blinks in the dark.")
print("-----------------------------------------------")
print("Start the game...")
print("Loading...")
print("-----------------------------------------------")
print("You see two ways out.")
print("To your left, there is a heavy steel door with a digital lock.")
print("To your right, there is a ventilation shaft")
print("-----------------------------------------------")
print("What do you choose?")
choiceofcrawl = input("Type 'door' to go through the door or 'vent' to go through the ventilation shaft: ").lower()
if choiceofcrawl == "vent":
    print("The shaft is narrow and dirty.")
    print("You crawl for a few minutes and find a strange electronic card.")
    print("It has a label: 'ACCESS_GRANTED_99'.")
    print("But wait! It is covered in dust. You need to clean it.")
    choiceofclean = input("Type 'clean' to clean the card (If you don't want to clean it, type 'ignore'): ").lower()
    if choiceofclean == "clean":
        print("Card cleaned, but it is still not working...")
        print("Oh no! The vent is closing! You need to hurry!")
        print("You try to crawl faster, but the vent is too narrow.")
        print("You get stuck and can't move!")
        print("Game Over!")
    elif choiceofclean == "ignore":
        print("You decide to ignore the card and keep crawling.")
        print("The vent is closing! You need to hurry!")
        print("You try to crawl faster, but the vent is too narrow.")
        print("You get stuck and can't move!")
        print("Game Over!")
    else:
        print("Invalid choice! Please in next time type 'clean' or 'ignore'.")
        print("Game Over!")
elif choiceofcrawl == "door":
    scrambledword = "!dlrow_olleh!"
    print("The digital lock requires a password.")
    print(f"Next to the door, you find a piece of paper with a strange scrambled word: '{scrambledword}'.")
    print("A note on the wall says: 'The password is this word, but reversed and without the first and last exclamation marks (!)'")
    print("You think for a very long time, but you still understand what the password should be and try to enter it.")
    password = scrambledword[-2 : 0 : -1]
    userpassword = input("Enter the password: ")
    if userpassword == password:
        print("The door opens! You step out into the sunlight and breathe fresh air.")
        print("Congratulations! You have escaped the laboratory!")
    else:
        print("Wrong password! The door remains locked.")
        print("You try to guess again, but you can't figure it out.")
        print("Time runs out and the laboratory's security system activates.")
        print("Game Over!")
else:
    print("Invalid choice! Please type 'door' or 'vent'.")
    print("Game Over!")

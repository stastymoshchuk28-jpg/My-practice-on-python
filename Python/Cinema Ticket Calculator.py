#done!

print("Welcome to the Cinema Ticket Calculator!")
print(" ")
name = input("What is your name? ")
print(" ")
people = int(input("How many people are in your group? "))
print(" ")
if people <= 0: #Single person buying a ticket
    print("You only have yourself, so you will be purchasing 1 ticket.")
    print(" ")
    age = int(input("What is your age? "))
    if age < 12: #Too young to buy a ticket
        print("You are too young to buy the ticket.")
        print(" ")
        print("You need be at least 12 years old to buy a ticket.")
        print(" ")
        print("Sorry, you cannot purchase a ticket.")
    elif age >= 12 and age <= 17: #Teenager buying a ticket
        print("Your ticket only costs $10. You get a discount because you are a teenager!")
    else: #Adult buying a ticket
        print("Your ticket costs $15. You do not get a discount because you are an adult.")
else: #Group buying tickets
    print(f"You have {people} people in your group, so you will be purchasing {people} tickets.")
    print(" ")
    age = int(input("What is the age of the persons purchasing the tickets? "))
    if age < 12: #Too young to buy a ticket
        print("You all are too young to buy the ticket.")
        print(" ")
        print("You all need be at least 12 years old to buy a ticket.")
        print(" ")
        print("Sorry, you all cannot purchase a ticket.")
    elif age >= 12 and age <= 17: #Teenager buying a ticket
        print("Your ticket only costs $10. You get a discount because you all are a teenager!")
    else: #Adult buying a ticket
        print("Your ticket costs $15. You do not get a discount because you all are adults.")

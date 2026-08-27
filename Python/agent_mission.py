#Done
#v1.0

import time

print("=== Welcome to the secret agency 'Shadow' ===")
print(" ")
coded_name = input("Enter your codename:")
time.sleep(1)
while True:
    print("Choose mission: ")
    print("1. - Mission 'secret labaratory' ")
    print("2. - Mission 'investigate an underground casino")
    print("3. - Exit")
    print(" ")
    choose = int(input("Choose number of mission: "))

    if choose == 1:
        print("You are going to the secret labaratory in forest...")
        print(" ")
        time.sleep(1)
        print("You hear - someone saying: 'Hey, anyone here? Help me, please!'.")
        print(" ")
        time.sleep(1)
        helping = input("Will you help this human? (Yes/no) ").lower()
        print(" ")
        if helping == "yes":
            time.sleep(1)
            print(f"{coded_name}, you running to his voice and find only body...")
            print(" ")
            time.sleep(1)
            print("You: 'No! I late, sorry man...'")
            print(" ")
            time.sleep(1)
            print("You run to labaratory, but hear something in bushes...")
            print(" ")
            time.sleep(1)
            checkingbushes = input("Will you check the bushes? (Yes/no) ").lower()
            print(" ")
            time.sleep(1)
            if checkingbushes == "yes":
                print("You going to bush...")
                print(" ")
                time.sleep(1)
                print("You check it and...")
                print(" ")
                time.sleep(1)
                print("You feel a breath behind your back...")
                print(" ")
                time.sleep(1)
                print("You were afraid to look back...")
                print(" ")
                time.sleep(1)
                print("You felt a terrible pain in your abdomen, as if you had been stabbed with a knife...")
                print(" ")
                time.sleep(1)
                print("You collapsed unconscious and died from blood loss...")
                print("Game over!")
                time.sleep(1)
                try_again = input("Do you want to try again? (Yes/no) ").lower()
                if try_again == "yes":
                    continue
                else:
                    print(" ")
                    print(f"Thanks for being in our agency, {coded_name}!")
                    print(" ")
                    time.sleep(1)
                    print("Thanks for playing!")
                    break
            elif checkingbushes == "no":
                print(" ")
                print("You don't checking bushes and run...")
                time.sleep(1)
                print(" ")
                print("You hear something leaping through the bushes, through the trees...")
                time.sleep(1)
                print(" ")
                print("You: I can't run faster! I hear it forward! What? I hear something at back...")
                time.sleep(1)
                print(" ")
                print("You: What is happening?!?! I hear it forward-back... That's creature playing with me?")
                time.sleep(1)
                print(" ")
                print("You: I want sleep... Why? No, that's gas!")
                time.sleep(1)
                print(" ")
                print("When you fell asleep, it ate you...")
                time.sleep(1)
                print(" ")
                try_again = input("Do you want to try again? (Yes/no) ").lower()
                if try_again == "yes":
                    continue
                else:
                    print(" ")
                    print(f"Thanks for being in our agency, {coded_name}!")
                    print(" ")
                    time.sleep(1)
                    print("Thanks for playing!")
                    break
        elif helping == "no" :
            print("You don't going on the voice and find labaratory!")
            time.sleep(1)
            print("But you have two options for how to get in: \n through the single window \n or through the door.")
            time.sleep(2.5)
            choose_to_in = input("Choose how to get in! (Door/window) ").lower()
            time.sleep(1)
            if choose_to_in == "door":
                print(" ")
                print("Door closed...")
                time.sleep(1)
                print(" ")
                print("You can want to get in through window...")
                time.sleep(1)
                print(" ")
                print("Oh no! It's closing!")
                time.sleep(1)
                print(" ")
                print("You try to fast get in, but window closed!")
                time.sleep(1)
                try_again = input("Do you want to try again? (Yes/no) ").lower()
                if try_again == "yes":
                    continue
                else:
                    print(" ")
                    print(f"Thanks for being in our agency, {coded_name}!")
                    print(" ")
                    time.sleep(1)
                    print("Thanks for playing!")
                    break
            elif choose_to_in == "window":
                print(" ")
                print("You going to the window and get in!")
                time.sleep(1)
                print(" ")
                print("You hear dialog:")
                time.sleep(1)
                print("Worker - Hello, Boss! I'm lefting labaratory.")
                time.sleep(1)
                print("Boss - Okay, doc.№254.")
                time.sleep(1)
                print("Worker - Goodbye!")
                time.sleep(1)
                print("Boss - Goodbye!")
                print(" ")
                time.sleep(1)
                print("Doc going to door!")
                print(" ")
                time.sleep(1)
                choose_to_hide = input("Where you want hide or go out? (Hide/go)").lower()
                print(" ")
                if choose_to_hide == "hide":
                    time.sleep(1)
                    print("You hiding behind the door.")
                    print(" ")
                    time.sleep(1)
                    print("He closed door and find you!")
                    time.sleep(1)
                    try_again = input("Do you want to try again? (Yes/no) ").lower()
                    if try_again == "yes":
                        continue
                    else:
                        print(" ")
                        print(f"Thanks for being in our agency, {coded_name}!")
                        print(" ")
                        time.sleep(1)
                        print("Thanks for playing!")
                        break
                elif choose_to_hide == "go":
                    time.sleep(1)
                    print("You want to go out...")
                    print(" ")
                    time.sleep(1)
                    print("But window closing!")
                    print(" ")
                    time.sleep(1)
                    print("You trying to go out, but...")
                    print(" ")
                    time.sleep(1)
                    print("It's closed!")
                    print(" ")
                    time.sleep(1)
                    print("Doc see you and kill!")
                    time.sleep(1)
                    try_again = input("Do you want to try again? (Yes/no) ").lower()
                    time.sleep(1)
                    if try_again == "yes":
                        continue
                    else:
                        print(" ")
                        print(f"Thanks for being in our agency, {coded_name}!")
                        print(" ")
                        time.sleep(1)
                        print("Thanks for playing!")
                        break
                else:
                    print("Not right choose!")
                    try_again = input("Do you want to try again? (Yes/no) ").lower()
                    if try_again == "yes":
                        continue
                    else:
                        print(" ")
                        print(f"Thanks for being in our agency, {coded_name}!")
                        print(" ")
                        time.sleep(1)
                        print("Thanks for playing!")
                        break
        else:
            print("Not right choose!")
            try_again = input("Do you want to try again? (Yes/no) ").lower()
            if try_again == "yes":
                continue
            else:
                print(" ")
                print(f"Thanks for being in our agency, {coded_name}!")
                print(" ")
                time.sleep(1)
                print("Thanks for playing!")
                break
    elif choose == 2:
        print("You are going to the casino.")
        print(" ")
        time.sleep(1)
        print("Door closed!")
        print(" ")
        time.sleep(1)
        print("You try to break down the door.")
        print(" ")
        time.sleep(1)
        print("That's metal!")
        print(" ")
        time.sleep(1)
        print("But you have a special machine with you - the 'Metal-Cutter X300A52'!")
        print(" ")
        time.sleep(1)
        open_door = input("You want to cut the door? (Yes/no) ").lower()
        print(" ")
        if open_door == "yes":
            print("You cutting the door!")
            print(" ")
            time.sleep(1)
            print("That's very loud!")
            print(" ")
            time.sleep(1)
            print("You hear something behind - it's shot from pistol!")
            print(" ")
            time.sleep(1)
            print("You died...")
            print(" ")
            time.sleep(1)
            try_again = input("Do you want to try again? (Yes/no) ").lower()
            time.sleep(1)
            if try_again == "yes":
                continue
            else:
                print(" ")
                print(f"Thanks for being in our agency, {coded_name}!")
                print(" ")
                time.sleep(1)
                print("Thanks for playing!")
                break
        elif open_door == "no":
            print("You go back to the agency...")
            print(" ")
            time.sleep(1)
            print("You back to agency!")
            continue
        else:
            print("Not right choose!")
            try_again = input("Do you want to try again? (Yes/no) ").lower()
            if try_again == "yes":
                continue
            else:
                print(" ")
                print(f"Thanks for being in our agency, {coded_name}!")
                print(" ")
                time.sleep(1)
                print("Thanks for playing!")
                break
    elif choose == 3:
        print("Thanks for playing!")
        break
    else:
        print("Not right number of mission!")
        print(" ")
        print("Try again!")
        continue
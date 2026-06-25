#Not done!

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
    elif choose == 2:
        print("You are going to the casino.")
        time.sleep(1)
        print("Door closed...")
        ...
    elif choose == 3:
        print("Thanks for playing!")
        break
    else:
        print("Not right number of mission!")
        print(" ")
        print("Try again!")
        continue

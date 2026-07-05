#Not done!
import time

while True:
    print("Choose what to do:")
    print("1. Write new text and analyze it!")
    print("2. Exit the proggram")
    choose_do = input("Choose number of action: ")
    if choose_do.isalpha():
        print("Choose can't be letter! Try again!")
        continue
    elif choose_do.isdigit():
        choose_do = int(choose_do)
        if choose_do == 1:
            text = input("Okay, firstly write the text: ")
        elif choose_do == 2:
            print("Thank's for using proggram!")
            print("Goodbye!")
            break
        else:
            print("Not right number! Try again!")
            continue
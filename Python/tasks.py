#It's enumerate pracite!
from time import sleep

tasks = ["Go to grocery shop", "Pass the exam with a score of 100", "Learn python"]

def oformity1():
    print(" ")
    sleep(0.5)

def oformity2():
    sleep(0.1)

def menu():
    print("=== Tasks ===")
    oformity1()
    print("1️⃣  1. Show tasks")
    oformity2()
    print("2️⃣  2. Complete task")
    oformity2()
    print("3️⃣  3. Exit")
    oformity1()
    menu_choice = input("⌨️  Enter your choice: ").strip()
    oformity1()
    if menu_choice.isdigit():
        continue_menu = False
        menu_choice = int(menu_choice)
        return menu_choice, continue_menu
    elif menu_choice == "":
        continue_menu = True
        print("❗ Choice can't be empty!")
        oformity1()
        return menu_choice, continue_menu
    else:
        continue_menu = True
        print("❗ Choice need to be number!")
        oformity1()
        return menu_choice, continue_menu

while True:
    menu_choice, continue_menu = menu()
    if continue_menu:
        continue
    else:
        if menu_choice == 1:
            ...
        elif menu_choice == 2:
            ...
        elif menu_choice == 3:
            ...
        else:
            print("")
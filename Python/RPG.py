#Not done!
#v0.9

from time import sleep, time
from random import randint

player_hp = 100
player_gold = 0
inventory = []

def oformity1():
    print(" ")
    sleep(0.5)

def oformity2():
    sleep(0.1)

def show_inventory(inventory):
    if not inventory:
        print("❗ Inventory is empty!")

print("👋 Welcome to the RPG!")
starter_time = time()
oformity1()
while True:
    print("=== RPG ===")
    oformity1()
    print("1️⃣  1. Show inventory")
    oformity2()
    print("2️⃣  2. Explore")
    oformity2()
    print("3️⃣  3. Use item")
    oformity2()
    print("4️⃣  4. Show stats")
    oformity2()
    print("5️⃣  5. Exit")
    oformity1()
    user_choice = input("⌨️  Enter your choice: ").strip()
    oformity1()
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice == 1:
            ...
        elif user_choice == 2:
            ...
        elif user_choice == 3:
            ...
        elif user_choice == 4:
            ...
        elif user_choice == 5:
            ...
        else:
            print("❗ Not right number of choice!")
            oformity1()
            continue
    elif user_choice == "":
        print("❗ Choice can't be empty!")
        oformity1()
        continue
    elif user_choice.isalpha():
        print("❗ Choice need to be number!")
        oformity1()
        continue
    else:
        print("❗ Choice need to be number!")
        oformity1()
        continue
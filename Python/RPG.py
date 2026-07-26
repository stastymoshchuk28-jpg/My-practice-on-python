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
    global oformity1, oformity2
    if not inventory:
        print("❗ Inventory is empty!")
        oformity1()
    else:
        print("🎒 Your inventory:")
        ryad = ""
        for item in inventory:
            ryad = ryad + item + "; \n"
        print(ryad[0: -2: 1])
        oformity1()

def explore(inventory):
    global oformity1, oformity2
    def find_random_item():
        random_item_num = randint(1, 8)
        if random_item_num == 1:
            random_item = "Apple"
            return random_item
        elif random_item_num == 2:
            random_item = "Potion"
            return random_item
        elif random_item_num == 3:
            random_item = "Iron Sword"
            return random_item
        elif random_item_num == 4:
            random_item = "Shield"
            return random_item
        elif random_item_num == 5:
            random_item = "Diamond"
            return random_item
        elif random_item_num == 6:
            random_item = "Bread"
            return random_item
        elif random_item_num == 7:
            random_item = "Wood"
            return random_item
        elif random_item_num == 8:
            random_item = "Gold Coin"
            return random_item

    random_item = find_random_item()
    print(f"✨ You explored the world and found {random_item}!")
    oformity1()
    print(f"➕ Item ({random_item}) add to inventory!")
    oformity1()
    inventory.append(random_item)
    return inventory

def use_item(inventory, player_hp, player_gold):
    if not inventory:
        print("❗ Inventory is empty, no items to use!")
        oformity1()
    else:
        while True:
            print("🎒 Your inventory: ", end="")
            ryad = ""
            for item in inventory:
                ryad = ryad + item + "; "
            print(ryad[0: -2: 1])
            oformity1()
            user_use = input("⌨️  Enter name of item to use: ").lower().strip()
            oformity1()
            for item in inventory:
                item_new = item.strip().lower()
                if item_new == user_use:
                    item_to_use = item
                    break
                else:
                    item_to_use = False
                    continue
            if item_to_use == False:
                print("❗ Not right name of item!")


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
            show_inventory(inventory)
        elif user_choice == 2:
            inventory = explore(inventory)
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
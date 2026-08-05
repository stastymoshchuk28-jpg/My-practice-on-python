#Not done!
#v0.9
from time import sleep
from random import randint

inventory = []

def oformity1():
    print(" ")
    sleep(0.5)

def oformity2():
    sleep(0.1)

def menu():
    print("=== Looting and inventory RPG ===")
    oformity1()
    print("1️⃣  1. Show inventory")
    oformity2()
    print("2️⃣  2. Find chest")
    oformity2()
    print("3️⃣  3. Count items")
    oformity2()
    print("4️⃣  4. Copy inventory")
    oformity2()
    print("5️⃣  5. Clear inventory")
    oformity2()
    print("6️⃣  6. Reverse inventory")
    oformity2()
    print("7️⃣  7. Exit")
    oformity1()

def show_inventory(inventory):
    if not inventory:
        print("❗ Your inventory is empty!")
        oformity1()
    else:
        text = ""
        for task in inventory:
            text = text + f"• {task};\n"
        text = text[0: -2: 1]
        print("🎒 Inventory:")
        oformity2()
        print(text)
        oformity1()

def found_chest(inventory):
    print("🏃 You go underground to search for a chest!")
    oformity1()
    found = randint(0, 1)
    if found == 0:
        print("✨ You found a chest!")
        oformity1()
        loot_variant = randint(0, 3)
        if loot_variant == 0:
            loot = ["Potion", "Shield"]
        elif loot_variant == 1:
            loot = ["Sword", "Bow"]
        elif loot_variant == 2:
            loot = ["Magic staff", "Apple"]
        elif loot_variant == 3:
            loot = ["Devil fruit", "Magic book"]
        text = ""
        for item in loot:
            text = text + item + ", "
        text = text[0: -2: 1]
        print(f"🌟 You opened the chest and found: {text}")
        oformity1()
        print("➕ Loot added to inventory!")
        inventory.extend(loot)
        oformity1()
        return inventory
    elif found == 1:
        print("❌ And... You don't find a chest...")
        oformity1()
        return inventory

def count_items(inventory):
    potion_f = False
    shield_f = False
    sword_f = False
    bow_f = False
    magic_staff_f = False
    apple_f = False
    devil_fruit_f = False
    magic_book_f = False

    text_found_items = ""
    
    print("🔎 Let's count item!")
    oformity1()
    for item in inventory:
        if item == "Potion":
            if potion_f != True:
                text_found_items = text_found_items + "Potion, "
                potion_f = True
        elif item == "Shield":
            if shield_f != True:
                text_found_items = text_found_items + "Shield, "
                shield_f = True
        elif item == "Sword":
            if sword_f != True:
                text_found_items = text_found_items + "Sword, "
                sword_f = True
        elif item == "Bow":
            if bow_f != True:
                text_found_items = text_found_items + "Bow, "
                bow_f = True
        elif item == "Magic staff":
            if magic_staff_f != True:
                text_found_items = text_found_items + "Magic staff, "
                magic_staff_f = True
        elif item == "Apple":
            if apple_f != True:
                text_found_items = text_found_items + "Apple, "
                apple_f = True
        elif item == "Devil fruit":
            if devil_fruit_f != True:
                text_found_items = text_found_items + "Devil fruit, "
                devil_fruit_f = True
        elif item == "Magic book":
            if magic_book_f != True:
                text_found_items = text_found_items + "Magic book, "
                magic_book_f = True
    print(f"🎒 Your found item:\n{text_found_items}")
    oformity1()
    

while True:
    menu()
    player_choice = input("⌨️  Enter your choice: ").strip()
    oformity1()
    if player_choice.isdigit():
        player_choice = int(player_choice)
        if player_choice == 1:
            show_inventory(inventory)
        elif player_choice == 2:
            inventory = found_chest(inventory)
        elif player_choice == 3:
            ...
        elif player_choice == 4:
            ...
        elif player_choice == 5:
            ...
        elif player_choice == 6:
            ...
        elif player_choice == 7:
            ...
        else:
            print("❗ Not right number of choice!")
            oformity1()
            continue
    elif player_choice == "":
        print("❗ Choice can't be empty!")
        oformity1()
        continue
    else:
        print("❗ Choice need to be a number!")
        oformity1()
        continue
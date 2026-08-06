#done!
#v1.0
from time import sleep
from random import randint

inventory = []
copy_of_inventory = []

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
    print("7️⃣  7. Change the inventory to a copy of it.")
    oformity2()
    print("8️⃣  8. Exit")
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
    if not inventory:
        print("❗ Inventory is empty!")
        oformity1()
    else:
        potion_f = False
        shield_f = False
        sword_f = False
        bow_f = False
        magic_staff_f = False
        apple_f = False
        devil_fruit_f = False
        magic_book_f = False
        number_of_item = 1

        text_found_items = ""
        
        print("🔎 Let's count item!")
        oformity1()
        for item in inventory:
            if item == "Potion":
                if potion_f != True:
                    text_found_items = text_found_items + f"{number_of_item}. Potion,\n"
                    potion_f = True
                    number_of_item += 1
            elif item == "Shield":
                if shield_f != True:
                    text_found_items = text_found_items + f"{number_of_item}. Shield,\n"
                    shield_f = True
                    number_of_item += 1
            elif item == "Sword":
                if sword_f != True:
                    text_found_items = text_found_items + f"{number_of_item}. Sword,\n"
                    sword_f = True
                    number_of_item += 1
            elif item == "Bow":
                if bow_f != True:
                    text_found_items = text_found_items + f"{number_of_item}. Bow,\n"
                    bow_f = True
                    number_of_item += 1
            elif item == "Magic staff":
                if magic_staff_f != True:
                    text_found_items = text_found_items + f"{number_of_item}. Magic staff,\n"
                    magic_staff_f = True
                    number_of_item += 1
            elif item == "Apple":
                if apple_f != True:
                    text_found_items = text_found_items + f"{number_of_item}. Apple,\n"
                    apple_f = True
                    number_of_item += 1
            elif item == "Devil fruit":
                if devil_fruit_f != True:
                    text_found_items = text_found_items + f"{number_of_item}. Devil fruit,\n"
                    devil_fruit_f = True
                    number_of_item += 1
            elif item == "Magic book":
                if magic_book_f != True:
                    text_found_items = text_found_items + f"{number_of_item}. Magic book,\n"
                    magic_book_f = True
                    number_of_item += 1

        text_found_items = text_found_items[0: -2: 1]
        print(f"🎒 Your found item:\n{text_found_items}")
        oformity1()
        user_choice = input("⌨️  Enter name of the item: ").strip()
        oformity1()
        if user_choice.isdigit():
            print("❗ Name can't be numbers!")
        elif user_choice == "":
            print("❗ Name can't be empty!")
            oformity1()
        else:
            if user_choice == "Potion" and potion_f:
                potions = inventory.count("Potion")
                print(f"🧪 Potions in inventory: {potions}")
                oformity1()
            elif user_choice == "Shield" and shield_f:
                shields = inventory.count("Shield")
                print(f"🛡️  Shields in inventory: {shields}")
                oformity1()
            elif user_choice == "Sword" and sword_f:
                swords = inventory.count("Sword")
                print(f"⚔️  Swords in inventory: {swords}")
                oformity1()
            elif user_choice == "Bow" and bow_f:
                bows = inventory.count("Bow")
                print(f"🏹 Bows in inventory: {bows}")
                oformity1()
            elif user_choice == "Magic staff" and magic_staff_f:
                magic_staffs = inventory.count("Magic staff")
                print(f"🪄  Magic staffs in inventory: {magic_staffs}")
                oformity1()
            elif user_choice == "Apple" and apple_f:
                apples = inventory.count("Apple")
                print(f"🍎 Apples in inventory: {apples}")
                oformity1()
            elif user_choice == "Devil fruit" and devil_fruit_f:
                devil_fruits = inventory.count("Devil fruit")
                print(f"🍈 Devil fruits in inventory: {devil_fruits}")
                oformity1()
            elif user_choice == "Magic book" and magic_book_f:
                magic_books = inventory.count("Magic book")
                print(f"📖 Magic books in inventory: {magic_books}")
                oformity1()
            else:
                print("❗ Not right name of the item!")
                oformity1()

def copy_inventory(inventory, copy_of_inventory):
    while True:
        if not inventory:
            print("❗ Inventory is empty! Nothing to copy!")
            oformity1()
            return copy_of_inventory
        print("💾 Creating inventory copy...")
        oformity1()
        if copy_of_inventory:
            print("❗ You already have copy of inventory!")
            oformity1()
            sure = input("❓ Are you sure to make new copy of inventory? (yes/no) ").strip().lower()
            oformity1()
            if sure == "yes":
                print("💾 Copy of inventory created!")
                copy_of_inventory = inventory.copy()
                oformity1()
                return copy_of_inventory
            elif sure == "no":
                print("❗ Copy creation cancelled!")
                oformity1()
                return copy_of_inventory
            else:
                print("❗ Not right word!")
                oformity1()
                continue
        else:
            print("💾 Copy of inventory created!")
            copy_of_inventory = inventory.copy()
            oformity1()
            return copy_of_inventory
        
def clear_inventory(inventory):
    while True:
        if not inventory:
            print("❗ Inventory is empty! Nothing to clear!")
            oformity1()
            return inventory
        else:
            print("🗑️  Clearing inventory...")
            oformity1()
            user_choice = input("❓ Are you sure to clear inventory? (yes/no) ").strip().lower()
            oformity1()
            if user_choice == "yes":
                print("🗑️  Inventory cleared!")
                inventory.clear()
                oformity1()
                return inventory
            elif user_choice == "no":
                print("❌ Inventory clearing cancelled!")
                oformity1()
                return inventory
            else:
                print("❗ Not right choice!")
                oformity1()
                continue

def reverse_inventory(inventory):
    while True:
        if not inventory:
            print("❗ Inventory is empty! Nothing to reverse!")
            oformity1()
            return inventory   
        else:
            print("🔄️ Reverse inventory...")  
            oformity1()
            user_choice = input("❓ Are you sure to reverse inventory? (yes/no) ").strip().lower()
            oformity1()
            if user_choice == "yes":
                print("🔄️ Inventory reversed!")
                inventory.reverse()
                oformity1()
                return inventory
            elif user_choice == "no":
                print("❌ Inventory reversed cancelled!")
                oformity1()
                return inventory
            else:
                print("❗ Not right choice!")
                oformity1()
                continue

def change_inventory_to_copy(inventory, copy_of_inventory):
    while True:
        if not copy_of_inventory:
            print("❗ The inventory copy is empty!")
            oformity1()
            return inventory
        else:
            print("🎒◀️ 💾 Changing the inventory to a copy of it...")
            oformity1()
            user_choice = input("❓ Are you sure to change inventory to a copy of it? (yes/no) ").strip().lower()
            oformity1()
            if user_choice == "yes":
                print("🎒◀️ 💾 Inventory changed to copy!")
                inventory = copy_of_inventory.copy()
                oformity1()
                return inventory
            elif user_choice == "no":
                print("❌ Inventory changing to copy cancelled!")
                oformity1()
                return inventory
            else:
                print("❗ Not right choice!")
                oformity1()
                continue

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
            count_items(inventory)
        elif player_choice == 4:
            copy_of_inventory = copy_inventory(inventory, copy_of_inventory)
        elif player_choice == 5:
            inventory = clear_inventory(inventory)
        elif player_choice == 6:
            inventory = reverse_inventory(inventory)
        elif player_choice == 7:
            inventory = change_inventory_to_copy(inventory, copy_of_inventory)
        elif player_choice == 8:
            show_inventory(inventory)
            print("👋 Goodbye!")
            break
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
#done!
#v1.0
from time import sleep
from random import randint

inventory = []
copy_of_inventory = []

def pause_long():
    print(" ")
    sleep(0.5)

def pause_short():
    sleep(0.1)

def menu():
    print("=== Looting and inventory RPG ===")
    pause_long()
    print("1️⃣  1. Show inventory")
    pause_short()
    print("2️⃣  2. Find chest")
    pause_short()
    print("3️⃣  3. Count items")
    pause_short()
    print("4️⃣  4. Copy inventory")
    pause_short()
    print("5️⃣  5. Clear inventory")
    pause_short()
    print("6️⃣  6. Reverse inventory")
    pause_short()
    print("7️⃣  7. Change the inventory to a copy of it.")
    pause_short()
    print("8️⃣  8. Exit")
    pause_long()

def show_inventory(inventory):
    if not inventory:
        print("❗ Your inventory is empty!")
        pause_long()
    else:
        text = ""
        for task in inventory:
            text = text + f"• {task};\n"
        text = text[0: -2: 1]
        print("🎒 Inventory:")
        pause_short()
        print(text)
        pause_long()

def found_chest(inventory):
    print("🏃 You go underground to search for a chest!")
    pause_long()
    found = randint(0, 1)
    if found == 0:
        print("✨ You found a chest!")
        pause_long()
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
        pause_long()
        print("➕ Loot added to inventory!")
        inventory.extend(loot)
        pause_long()
        return inventory
    elif found == 1:
        print("❌ And... You don't find a chest...")
        pause_long()
        return inventory

def count_items(inventory):
    if not inventory:
        print("❗ Inventory is empty!")
        pause_long()
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
        pause_long()
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
        pause_long()
        user_choice = input("⌨️  Enter name of the item: ").strip()
        pause_long()
        if user_choice.isdigit():
            print("❗ Name can't be numbers!")
        elif user_choice == "":
            print("❗ Name can't be empty!")
            pause_long()
        else:
            if user_choice == "Potion" and potion_f:
                potions = inventory.count("Potion")
                print(f"🧪 Potions in inventory: {potions}")
                pause_long()
            elif user_choice == "Shield" and shield_f:
                shields = inventory.count("Shield")
                print(f"🛡️  Shields in inventory: {shields}")
                pause_long()
            elif user_choice == "Sword" and sword_f:
                swords = inventory.count("Sword")
                print(f"⚔️  Swords in inventory: {swords}")
                pause_long()
            elif user_choice == "Bow" and bow_f:
                bows = inventory.count("Bow")
                print(f"🏹 Bows in inventory: {bows}")
                pause_long()
            elif user_choice == "Magic staff" and magic_staff_f:
                magic_staffs = inventory.count("Magic staff")
                print(f"🪄  Magic staffs in inventory: {magic_staffs}")
                pause_long()
            elif user_choice == "Apple" and apple_f:
                apples = inventory.count("Apple")
                print(f"🍎 Apples in inventory: {apples}")
                pause_long()
            elif user_choice == "Devil fruit" and devil_fruit_f:
                devil_fruits = inventory.count("Devil fruit")
                print(f"🍈 Devil fruits in inventory: {devil_fruits}")
                pause_long()
            elif user_choice == "Magic book" and magic_book_f:
                magic_books = inventory.count("Magic book")
                print(f"📖 Magic books in inventory: {magic_books}")
                pause_long()
            else:
                print("❗ Not right name of the item!")
                pause_long()

def copy_inventory(inventory, copy_of_inventory):
    while True:
        if not inventory:
            print("❗ Inventory is empty! Nothing to copy!")
            pause_long()
            return copy_of_inventory
        print("💾 Creating inventory copy...")
        pause_long()
        if copy_of_inventory:
            print("❗ You already have copy of inventory!")
            pause_long()
            sure = input("❓ Are you sure to make new copy of inventory? (yes/no) ").strip().lower()
            pause_long()
            if sure == "yes":
                print("💾 Copy of inventory created!")
                copy_of_inventory = inventory.copy()
                pause_long()
                return copy_of_inventory
            elif sure == "no":
                print("❗ Copy creation cancelled!")
                pause_long()
                return copy_of_inventory
            else:
                print("❗ Not right word!")
                pause_long()
                continue
        else:
            print("💾 Copy of inventory created!")
            copy_of_inventory = inventory.copy()
            pause_long()
            return copy_of_inventory
        
def clear_inventory(inventory):
    while True:
        if not inventory:
            print("❗ Inventory is empty! Nothing to clear!")
            pause_long()
            return inventory
        else:
            print("🗑️  Clearing inventory...")
            pause_long()
            user_choice = input("❓ Are you sure to clear inventory? (yes/no) ").strip().lower()
            pause_long()
            if user_choice == "yes":
                print("🗑️  Inventory cleared!")
                inventory.clear()
                pause_long()
                return inventory
            elif user_choice == "no":
                print("❌ Inventory clearing cancelled!")
                pause_long()
                return inventory
            else:
                print("❗ Not right choice!")
                pause_long()
                continue

def reverse_inventory(inventory):
    while True:
        if not inventory:
            print("❗ Inventory is empty! Nothing to reverse!")
            pause_long()
            return inventory   
        else:
            print("🔄️ Reverse inventory...")  
            pause_long()
            user_choice = input("❓ Are you sure to reverse inventory? (yes/no) ").strip().lower()
            pause_long()
            if user_choice == "yes":
                print("🔄️ Inventory reversed!")
                inventory.reverse()
                pause_long()
                return inventory
            elif user_choice == "no":
                print("❌ Inventory reversed cancelled!")
                pause_long()
                return inventory
            else:
                print("❗ Not right choice!")
                pause_long()
                continue

def change_inventory_to_copy(inventory, copy_of_inventory):
    while True:
        if not copy_of_inventory:
            print("❗ The inventory copy is empty!")
            pause_long()
            return inventory
        else:
            print("🎒◀️ 💾 Changing the inventory to a copy of it...")
            pause_long()
            user_choice = input("❓ Are you sure to change inventory to a copy of it? (yes/no) ").strip().lower()
            pause_long()
            if user_choice == "yes":
                print("🎒◀️ 💾 Inventory changed to copy!")
                inventory = copy_of_inventory.copy()
                pause_long()
                return inventory
            elif user_choice == "no":
                print("❌ Inventory changing to copy cancelled!")
                pause_long()
                return inventory
            else:
                print("❗ Not right choice!")
                pause_long()
                continue

while True:
    menu()
    player_choice = input("⌨️  Enter your choice: ").strip()
    pause_long()
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
            pause_long()
            continue
    elif player_choice == "":
        print("❗ Choice can't be empty!")
        pause_long()
        continue
    else:
        print("❗ Choice need to be a number!")
        pause_long()
        continue
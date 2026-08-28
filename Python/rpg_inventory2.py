#Done
#v1.0

from time import sleep
inventory = []
picked_items = []

def pause_long():
    print(" ")
    sleep(0.5)

def pause_short():
    sleep(0.1)

def menu():
    print("=== RPG inventory ===")
    pause_long()
    print("1️⃣  1. Show inventory")
    pause_short()
    print("2️⃣  2. Pick up item")
    pause_short()
    print("3️⃣  3. Put item in slot")
    pause_short()
    print("4️⃣  4. Drop item")
    pause_short()
    print("5️⃣  5. Sort inventory")
    pause_short()
    print("6️⃣  6. Exit")
    pause_long()
    player_choice = input("⌨️  Enter your choice: ").strip()
    pause_long()
    return player_choice

def show_inventory(inventory):
    if not inventory:
        print("❗ Inventory is empty!")
        pause_long()
    else:
        print("📦 Your inventory: ")
        pause_short()
        text = ""
        for item in inventory:
            text = text + f"{inventory.index(item)+1}. {item};\n"
        text = text[0: -2: 1]
        print(text)
        pause_long()

def pick_up_item(inventory, picked_items):
    while True:
        item_name = input("⌨️  Enter item name to add it: ").strip()
        pause_long()
        if item_name.isdigit():
            print("❗ Item name can't be only number!")
            pause_long()
            continue
        elif item_name == "":
            print("❗ Item can't be empty!")
            pause_long()
            continue
        else:
            if item_name in inventory:
                print("❗ Item already in inventory!")
                pause_long()
                continue
            else:
                if not item_name in picked_items:
                    picked_items.append(item_name)
                    print("📦 You pick up item. Now you can add it to inventory!")
                    pause_long()
                    return picked_items
                else:
                    print("❗ Item already picked!")
                    pause_long()
                    continue

def put_item_in_slot(inventory, picked_items):
    while True:
        if not picked_items:
            print("❗ You don't pick up any items!")
            pause_long()
            return inventory, picked_items
        print("📦 Picked items: ", end="")
        text = ""
        for item in picked_items:
            text = text + f"{item}; "
        text = text[0: -2: 1]
        print(text)
        pause_long()
        item_name = input("⌨️  Enter item name: ").strip()
        pause_long()
        in_inventory = False
        for item in inventory:
            check_name_ii = item.lower()
            item_name_to_check = item_name.lower()
            if item_name_to_check == check_name_ii:
                in_inventory = True
                break
            else:
                in_inventory = False
                continue
        in_p_i = False
        for item in picked_items:
            check_name_ip_i = item.lower()
            item_name_to_check = item_name.lower()
            if item_name_to_check == check_name_ip_i:
                in_p_i = True
                break
            else:
                in_p_i = False
                continue
        if in_p_i:
            if in_inventory:
                print("❗ Item in inventory!")
                pause_long()
                continue
            item_slot = input("⌨️  Enter item slot (number): ").strip()
            pause_long()
            if item_slot.isdigit():
                item_slot = int(item_slot)
                if item_slot <= 0 or item_slot < 1:
                    print("❗ Not right slot number")
                    pause_long()
                    continue
                else:
                    if (item_slot - 1) > len(inventory):
                        print(f"❗ Invalid slot! Choose a slot from 1 to {len(inventory) + 1}.")
                        pause_long()
                        continue
                    else:
                        slot = item_slot - 1
                        inventory.insert(slot, item_name)
                        picked_items.remove(item_name)
                        print(f"➕ Item {item_name} added to slot {item_slot}!")
                        pause_long()
                        return inventory, picked_items
            elif item_slot == "":
                print("❗ Item slot can't be empty!")
                pause_long()
                continue
            else:
                print("❗ Item slot need to be a number!")
                pause_long()
                continue
        else:
            print("❗ Item not picked!")
            pause_long()
            continue

def drop_item(inventory):
    while True:
        if not inventory:
            print("❗ Inventory is empty! Can't delete any item!")
            pause_long()
            return inventory
        text = ""
        print("=== Drop item ===")
        pause_long()
        for item in inventory:
            item_index = inventory.index(item) + 1
            text = text + f"{item_index}. {item};\n"
        text = text[0: -2: 1]
        print(text)
        pause_long()
        user_choice_to_drop = input("⌨️  Enter your choice: ").strip()
        pause_long()
        if user_choice_to_drop.isdigit():
            user_choice_to_drop = int(user_choice_to_drop)
            delete_index = user_choice_to_drop - 1
            if delete_index < 0:
                print("❗ No item in this slot!")
                pause_long()
                continue
            elif delete_index >= len(inventory):
                print("❗ No item in this slot!")
                pause_long()
                continue
            else:
                item_to_delete = inventory[delete_index]
                inventory.pop(delete_index)
                print(f"🗑️  Item {item_to_delete} deleted!")
                pause_long()
                return inventory
        elif user_choice_to_drop == "":
            print("❗ Choice can't be empty!")
            pause_long()
            continue
        else:
            print("❗ Choice need to be number!")
            pause_long()
            continue

def sort_inventory(inventory):
    while True:
        if not inventory:
            print("❗ Inventory is empty! Can't sort it!")
            pause_long()
            return inventory
        print("=== Sort inventory ===")
        pause_long()
        print("1️⃣  1. Sort by A-Z")
        print("2️⃣  2. Sort by Z-A")
        pause_long()
        user_choice_to_sort = input("⌨️  Enter your choice: ").strip()
        pause_long()
        if user_choice_to_sort.isdigit():
            user_choice_to_sort = int(user_choice_to_sort)
            if user_choice_to_sort == 1:
                inventory.sort(key=str.lower)
                print("✨ Inventory sorted!")
                pause_long()
                return inventory
            elif user_choice_to_sort == 2:
                inventory.sort(key=str.lower, reverse=True)
                print("✨ Inventory sorted!")
                pause_long()
                return inventory
            else:
                print("❗ Not right number of choice!")
                pause_long()
                continue
        elif user_choice_to_sort == "":
            print("❗ Choice can't be empty!")
            pause_long()
            continue
        else:
            print("❗ Choice need to be number!")
            pause_long()
            continue

def exit_program(inventory):
    show_inventory(inventory)
    print("👋 Goodbye!")
    pause_long()
    exit()

while True:
    player_choice = menu()
    if player_choice.isdigit():
        player_choice = int(player_choice)
        if player_choice == 1:
            show_inventory(inventory)
        elif player_choice == 2:
            picked_items = pick_up_item(inventory, picked_items)
        elif player_choice == 3:
            inventory, picked_items = put_item_in_slot(inventory, picked_items)
        elif player_choice == 4:
            inventory = drop_item(inventory)
        elif player_choice == 5:
            inventory = sort_inventory(inventory)
        elif player_choice == 6:
            exit_program(inventory)
        else:
            print("❗ Not right number of choice!")
            pause_long()
            continue
    elif player_choice == "":
        print("❗ Choice can't be empty!")
        pause_long()
        continue
    else:
        print("❗ Choice need to be number!")
        pause_long()
        continue
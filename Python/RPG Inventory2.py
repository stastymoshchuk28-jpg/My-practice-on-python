from time import sleep
inventory = []
picked_items = []

def oformity1():
    print(" ")
    sleep(0.5)

def oformity2():
    sleep(0.1)

def menu():
    print("=== RPG inventory ===")
    oformity1()
    print("1️⃣  1. Show inventory")
    oformity2()
    print("2️⃣  2. Pick up item")
    oformity2()
    print("3️⃣  3. Put item in slot")
    oformity2()
    print("4️⃣  4. Drop item")
    oformity2()
    print("5️⃣  5. Sort inventory")
    oformity2()
    print("6️⃣  6. Exit")
    oformity1()
    player_choice = input("⌨️  Enter your choice: ").strip()
    oformity1()
    return player_choice

def show_inventory(inventory):
    if not inventory:
        print("❗ Inventory is empty!")
        oformity1()
    else:
        print("📦 Your inventory: ")
        oformity2()
        text = ""
        for item in inventory:
            text = text + f"{inventory.index(item)+1}. {item};\n"
        text = text[0: -2: 1]
        print(text)
        oformity1()

def pick_up_item(inventory, picked_items):
    while True:
        item_name = input("⌨️  Enter item name to add it: ").strip()
        oformity1()
        if item_name.isdigit():
            print("❗ Item name can't be only number!")
            oformity1()
            continue
        elif item_name == "":
            print("❗ Item can't be empty!")
            oformity1()
            continue
        else:
            if item_name in inventory:
                print("❗ Item already in inventory!")
                oformity1()
                continue
            else:
                if not item_name in picked_items:
                    picked_items.append(item_name)
                    print("📦 You pick up item. Now you can add it to inventory!")
                    oformity1()
                    return picked_items
                else:
                    print("❗ Item already picked!")
                    oformity1()
                    continue

def put_item_in_slot(inventory, picked_items):
    while True:
        if not picked_items:
            print("❗ You don't pick up any items!")
            oformity1()
            return inventory, picked_items
        print("📦 Picked items: ", end="")
        text = ""
        for item in picked_items:
            text = text + f"{item}; "
        text = text[0: -2: 1]
        print(text)
        oformity1()
        item_name = input("⌨️  Enter item name: ").strip()
        oformity1()
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
                oformity1()
                continue
            item_slot = input("⌨️  Enter item slot (number): ").strip()
            if item_slot.isdigit():
                item_slot = int(item_slot)
                if item_slot <= 0 or item_slot < 1:
                    print("❗ Not right slot number")
                    oformity1()
                    continue
                else:
                    if (item_slot - 1) > len(inventory):
                        print(f"❗ Invalid slot! Choose a slot from 1 to {len(inventory) + 1}.")
                        oformity1()
                        continue
                    else:
                        slot = item_slot - 1
                        inventory.insert(slot, item_name)
                        picked_items.remove(item_name)
                        print(f"➕ Item {item_name} added to slot {item_slot}!")
                        oformity1()
                        return inventory, picked_items
            elif item_slot == "":
                print("❗ Item slot can't be empty!")
                oformity1()
                continue
            else:
                print("❗ Item slot need to be a number!")
                oformity1()
                continue
        else:
            print("❗ Item not picked!")
            oformity1()
            continue

def drop_item(inventory, picked_items):
    while True:
        print("=== Drop item ===")
        oformity1()
        print("1️⃣  1. drop from inventory")
        oformity2()
        print("2️⃣  2. drop from picked items")
        oformity1()
        user_choice_to_drop = input("⌨️  Enter your choice: ").strip()
        oformity1()
        if user_choice_to_drop.isdigit():
            user_choice_to_drop = int(user_choice_to_drop)
            if user_choice_to_drop == 1:
                ...
            elif user_choice_to_drop == 2:
                ...
        elif user_choice_to_drop == "":
            print("❗ Choice can't be empty!")
            oformity1()
            continue
        else:
            print("❗ Choice need to be number!")
            oformity1()
            continue

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
            ...
        elif player_choice == 5:
            ...
        elif player_choice == 6:
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
        print("❗ Choice need to be number!")
        oformity1()
        continue
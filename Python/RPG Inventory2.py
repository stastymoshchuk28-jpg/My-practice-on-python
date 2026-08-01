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
            text = text + f"{item};\n"
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
                print("❗ Item alredy in inventory!")
                oformity1()
                continue
            else:
                if not item_name in picked_items:
                    slot = None
                    item = [item_name, slot]
                    picked_items.append(item)
                    oformity1()
                    print("📦 You pick up item. Now you can add it to inventory!")
                    oformity1()
                    return picked_items
                else:
                    print("❗ Item alredy picked!")
                    oformity1()
                    continue

def put_item_in_slot(inventory, picked_items):
    while True:
        if not picked_items:
            print("❗ You don't pick up any items!")
            oformity1()
            return inventory
        print("📦 Picked items: ", end="")
        text = ""
        for item in picked_items:
            text = text + f"{item[0]}; "
        print(text)
        oformity1()
        item_name = input("⌨️  Enter item name: ").strip()
        oformity1()
        if item_name in inventory:
            print("❗ Item in inventory!")
            oformity1()
            continue
        item_slot = input("⌨️  Enter item slot (number): ").strip()
        if item_slot <= 0:
            print("❗ Not right slot number")
            oformity1()
            continue
        else:
            ...


while True:
    player_choice = menu()
    if player_choice.isdigit():
        player_choice = int(player_choice)
        if player_choice == 1:
            ...
        elif player_choice == 2:
            ...
        elif player_choice == 3:
            ...
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
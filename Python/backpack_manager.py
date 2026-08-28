#Done
#v1.0

from time import sleep

backpack = []
finded_items = []

def pause_long():
    print(" ")
    sleep(0.5)

def pause_short():
    sleep(0.1)

def view_backpack(backpack):
    global pause_long, pause_short
    if backpack == []:
        print("❗ Your backpack is empty!")
        pause_long()
    else:
        print("🎒 Your backpack:")
        pause_long()
        for item in backpack:
            print(item)
            pause_short()
        pause_long()

def add_item(finded_items, backpack):
    global pause_long, pause_short
    if finded_items == []:
        print("❗ You don't have finded items!")
        pause_long()
        return backpack, finded_items
    else:
        while True:
            print("✨ Your finded items: ", end="")
            ryad = ""
            for item in finded_items:
                ryad = ryad + item + ", "
            ryad = ryad[0: -2: 1]
            print(ryad)
            print(" ")
            pause_long()
            user_choice = input("⌨️  Enter item name to add it into backpack: ").lower()
            user_choice = user_choice.strip()
            pause_long()
            if user_choice.isdigit():
                print("❗ Item name can't be number!")
                pause_long()
                continue
            elif user_choice == "":
                print("❗ Item name can't be empty!")
                pause_long()
                continue
            else:
                if user_choice in finded_items:
                    for item in finded_items: 
                        item_nc = item.strip() 
                        item_c = item_nc.lower() 
                        if user_choice == item_c: 
                            item_to_del = item 
                            break 
                        else: 
                            continue
                    if user_choice in backpack:
                        print("❗ Item in backpack!")
                    else:
                        print("➕ Item added to backpack!")
                        backpack.append(item.capitalize())
                        finded_items.remove(item_to_del)
                    pause_long()
                    return backpack, finded_items
                else:
                    print("❗ Item not in finded items!")
                    pause_long()
                    continue

def remove_item(backpack):
    global pause_long, pause_short
    if backpack == []:
        print("❗ You don't have items in backpack to remove it!")
        pause_long()
        return backpack
    else:
        while True:
            print("✨ Your items in backpack: ", end="")
            ryad = ""
            for item in backpack:
                ryad = ryad + item + ", "
            ryad = ryad[0: -2: 1]
            print(ryad)
            print(" ")
            pause_long()
            user_choice = input("⌨️  Enter item name to remove it from backpack: ").lower()
            user_choice = user_choice.strip()
            pause_long()
            if user_choice.isdigit():
                print("❗ Item name can't be number!")
                pause_long()
                continue
            elif user_choice == "":
                print("❗ Item name can't be empty!")
                pause_long()
                continue
            else:
                for item in backpack: 
                    item_nc = item.strip() 
                    item_c = item_nc.lower() 
                    if user_choice == item_c: 
                        item_to_del = item
                        break 
                    else: 
                        continue
                if user_choice == item_c:
                    print("➖ Item removed from backpack!")
                    backpack.remove(item_to_del)
                    pause_long()
                    return backpack
                else:
                    print("❗ Item not in backpack!")
                    pause_long()
                    continue

def search_item(finded_items):
    while True:
        user_finding = input("⌨️  Enter what you want to find: ").lower()
        user_finding = user_finding.strip()
        pause_long()
        if user_finding != "" and not user_finding.isdigit():
            if not user_finding in finded_items:
                print(f"✨ You found {user_finding} and go. You can add it into your backpack now!")
                pause_long()
                finded_items.append(user_finding)
                return finded_items
            else:
                print(f"❗ Item - {user_finding} in finded items you can't add it!")
                pause_long()
                continue
        else:
            if user_finding == "":
                print("❗ Item to find can't be empty!")
                pause_long()
                continue
            elif user_finding.isdigit():
                print("❗ Item to find can't be number!")
                pause_long()
                continue

print("=== Backpack Manager ===")
pause_long()
while True:
    print("1️⃣  1. View backpack")
    pause_short()
    print("2️⃣  2. Add item")
    pause_short()
    print("3️⃣  3. Remove item")
    pause_short()
    print("4️⃣  4. Search item")
    pause_short()
    print("5️⃣  5. Exit")
    pause_long()
    user_choice = input("⌨️  Enter your choice: ")
    pause_long()
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice == 1:
            view_backpack(backpack)
        elif user_choice == 2:
            backpack, finded_items = add_item(finded_items, backpack)
        elif user_choice == 3:
            backpack = remove_item(backpack)
        elif user_choice == 4:
            finded_items = search_item(finded_items)
        elif user_choice == 5:
            ryad = ""
            for item in backpack:
                ryad = ryad + item + ", "
            ryad = ryad[0: -2: 1]
            print(f"🎒 Your backpack: {ryad}")
            pause_long()
            print("👋 Thank you for using Backpack Manager! Goodbye!")
            break
        else:
            print("❗ Not right number of choice!")
            pause_long()
            continue
    elif user_choice.strip() == "":
        print("❗ Choice can't be empty")
        pause_long()
        continue
    else:
        print("❗ Choice need to be number!")
        pause_long()
        continue

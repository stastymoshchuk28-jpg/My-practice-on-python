#Done

from time import sleep

backpack = []
finded_items = []

def oformity1():
    print(" ")
    sleep(0.5)

def oformity2():
    sleep(0.1)

def view_backpack(backpack):
    global oformity1, oformity2
    if backpack == []:
        print("❗ Your backpack is empty!")
        oformity1()
    else:
        print("🎒 Your backpack:")
        oformity1()
        for item in backpack:
            print(item)
            oformity2()
        oformity1()

def add_item(finded_items, backpack):
    global oformity1, oformity2
    if finded_items == []:
        print("❗ You don't have finded items!")
        oformity1()
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
            oformity1()
            user_choice = input("⌨️  Enter item name to add it into backpack: ").lower()
            user_choice = user_choice.strip()
            oformity1()
            if user_choice.isdigit():
                print("❗ Item name can't be number!")
                oformity1()
                continue
            elif user_choice == "":
                print("❗ Item name can't be empty!")
                oformity1()
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
                    oformity1()
                    return backpack, finded_items
                else:
                    print("❗ Item not in finded items!")
                    oformity1()
                    continue

def remove_item(backpack):
    global oformity1, oformity2
    if backpack == []:
        print("❗ You don't have items in backpack to remove it!")
        oformity1()
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
            oformity1()
            user_choice = input("⌨️  Enter item name to remove it from backpack: ").lower()
            user_choice = user_choice.strip()
            oformity1()
            if user_choice.isdigit():
                print("❗ Item name can't be number!")
                oformity1()
                continue
            elif user_choice == "":
                print("❗ Item name can't be empty!")
                oformity1()
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
                    oformity1()
                    return backpack
                else:
                    print("❗ Item not in backpack!")
                    oformity1()
                    continue

def search_item(finded_items):
    while True:
        user_finding = input("⌨️  Enter what you want to find: ").lower()
        user_finding = user_finding.strip()
        oformity1()
        if user_finding != "" and not user_finding.isdigit():
            if not user_finding in finded_items:
                print(f"✨ You found {user_finding} and go. You can add it into your backpack now!")
                oformity1()
                finded_items.append(user_finding)
                return finded_items
            else:
                print(f"❗ Item - {user_finding} in finded items you can't add it!")
                oformity1()
                continue
        else:
            if user_finding == "":
                print("❗ Item to find can't be empty!")
                oformity1()
                continue
            elif user_finding.isdigit():
                print("❗ Item to find can't be number!")
                oformity1()
                continue

print("=== Backpack Manager ===")
oformity1()
while True:
    print("1️⃣  1. View backpack")
    oformity2()
    print("2️⃣  2. Add item")
    oformity2()
    print("3️⃣  3. Remove item")
    oformity2()
    print("4️⃣  4. Search item")
    oformity2()
    print("5️⃣  5. Exit")
    oformity1()
    user_choice = input("⌨️  Enter your choice: ")
    oformity1()
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
            oformity1()
            print("👋 Thank you for using Backpack Manager! Goodbye!")
            break
    elif user_choice.strip() == "":
        print("❗ Choice can't be empty")
        continue
    else:
        print("❗ Choice need to be number!")
        continue

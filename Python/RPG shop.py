from time import sleep

player = {
    "Inventory": [],
    "Money": 1000
}

shop = {
    "Apple": {"Cost": 10, "Stock": 4},
    "Potion": {"Cost": 50, "Stock": 2},
    "Shield": {"Cost": 125, "Stock": 1},
    "Sword": {"Cost": 100, "Stock": 3},
    "Bow": {"Cost": 75, "Stock": 1},
    "Magic book": {"Cost": 200, "Stock": 2}
}

def oformity1():
    print(" ")
    sleep(0.5)

def oformity2():
    sleep(0.1)

def menu():
    print("=== RPG shop ===")
    oformity1()
    print("1️⃣  1. Show shop")
    oformity2()
    print("2️⃣  2. Buy item")
    oformity2()
    print("3️⃣  3. Show your inventory")
    oformity2()
    print("4️⃣  4. Show your money")
    oformity2()
    print("5️⃣  5. Exit")
    oformity1()

def show_shop(shop):
    print("🛒 Shop: ")
    oformity1()
    for num_of_item, (item, item_info) in enumerate(shop.items(), start=1):
        cost_of_item = item_info["Cost"]
        stock_of_item = item_info["Stock"]

        print(f"{num_of_item}. {item}")
        oformity2()
        print(f"💰 Cost: {cost_of_item}")
        oformity2()
        print(f"📊 Stock: {stock_of_item}")
        oformity1()

def buy_item(shop, player):
    player_inventory = player["Inventory"]
    while True:
        show_shop(shop)
        user_choice = input("⌨️  Enter item name to buy it: ").strip().capitalize()
        oformity1()
        if user_choice.isdigit():
            print("❗ Item name can't be only numbers")
            oformity1()
            continue
        elif user_choice == "":
            print("❗ Item name can't be empty!")
            oformity1()
            continue
        else:
            item_found = False
            for item_name, item_info in shop.items():
                if item_name == user_choice:
                    item_to_buy = item_name
                    item_cost = item_info["Cost"]
                    item_found = True
                    break
            if item_found:
                if shop[item_to_buy]["Stock"] > 0:
                    if player["Money"] < item_cost:
                        print(f"❗ You don't have money to buy {item_to_buy}")
                        oformity1()
                        return shop, player
                    else:
                        print(f"✅ {item_to_buy} bought!")
                        oformity1()
                        shop[item_to_buy]["Stock"] -= 1
                        player["Money"] -= item_cost
                        need_to_add_item = True
                        if player_inventory:
                            for item in player_inventory:
                                item_name = item["Item name"]
                                if item_name == item_to_buy:
                                    item["Items"] += 1
                                    need_to_add_item = False
                                    break
                        if need_to_add_item:
                            item_to_add = {"Item name": item_to_buy, "Items": 1}
                            player_inventory.append(item_to_add)
                            return shop, player
                        else:
                            return shop, player
                else:
                    print(f"❗ No left {item_to_buy} in shop!")
                    oformity1()
                    return shop, player
            else:
                print("❗ Item not in shop!")
                oformity1()
                continue

while True:
    menu()
    user_choice = input("⌨️  Enter your choice: ").strip()
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice == 1:
            show_shop(shop)
        elif user_choice == 2:
            shop, player = buy_item(shop, player)
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
    else:
        print("❗ Choice need to be a number")
        oformity1()
        continue
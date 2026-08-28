#done!
#v1.0
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

def pause_long():
    print(" ")
    sleep(0.5)

def pause_short():
    sleep(0.1)

def menu():
    print("=== RPG shop ===")
    pause_long()
    print("1️⃣  1. Show shop")
    pause_short()
    print("2️⃣  2. Buy item")
    pause_short()
    print("3️⃣  3. Show your inventory")
    pause_short()
    print("4️⃣  4. Show your money")
    pause_short()
    print("5️⃣  5. Exit")
    pause_long()

def show_shop(shop):
    print("🛒 Shop: ")
    pause_long()
    for num_of_item, (item, item_info) in enumerate(shop.items(), start=1):
        cost_of_item = item_info["Cost"]
        stock_of_item = item_info["Stock"]

        print(f"{num_of_item}. {item}")
        pause_short()
        print(f"💰 Cost: {cost_of_item}")
        pause_short()
        print(f"📊 Stock: {stock_of_item}")
        pause_long()

def buy_item(shop, player):
    player_inventory = player["Inventory"]
    while True:
        show_shop(shop)
        user_choice = input("⌨️  Enter item name to buy it: ").strip().capitalize()
        pause_long()
        if user_choice.isdigit():
            print("❗ Item name can't be only numbers")
            pause_long()
            continue
        elif user_choice == "":
            print("❗ Item name can't be empty!")
            pause_long()
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
                        pause_long()
                        return shop, player
                    else:
                        print(f"✅ {item_to_buy} bought!")
                        pause_long()
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
                    pause_long()
                    return shop, player
            else:
                print("❗ Item not in shop!")
                pause_long()
                continue

def show_inventory(player):
    player_inventory = player["Inventory"]
    if not player_inventory:
        print("❗ Your inventory empty!")
        pause_long()
    else:
        text = ""
        for item in player_inventory:
            item_name = item["Item name"]
            items = item["Items"]

            text = text + f"• {item_name}: {items}\n"
        text = text[0: -1: 1]
        print("🎒 Your inventory: ")
        pause_long()
        print(text)
        pause_long()

def show_money(player):
    print(f"💰 Your money: {player['Money']}")
    pause_long()

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
            show_inventory(player)
        elif user_choice == 4:
            show_money(player)
        elif user_choice == 5:
            show_inventory(player)
            show_money(player)
            print("👋 Goodbye!")
            break
        else:
            print("❗ Not right number of choice!")
            pause_long()
            continue
    elif user_choice == "":
        print("❗ Choice can't be empty!")
        pause_long()
        continue
    else:
        print("❗ Choice need to be a number")
        pause_long()
        continue
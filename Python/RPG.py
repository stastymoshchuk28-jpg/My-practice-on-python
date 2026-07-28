#done!

from time import sleep, time
from random import randint

player_hp = 100
player_gold = 0
shield_used = False
inventory = []

def oformity1():
    print(" ")
    sleep(0.5)

def oformity2():
    sleep(0.1)

def check_dead(player_hp):
    if player_hp <= 0:
        dead = True
        return dead
    else:
        dead = False
        return dead

def show_inventory(inventory):
    if not inventory:
        print("❗ Inventory is empty!")
        oformity1()
    else:
        print("🎒 Your inventory:")
        ryad = ""
        for item in inventory:
            ryad = ryad + item + "; \n"
        print(ryad[0: -2: 1])
        oformity1()

def explore(inventory):
    def find_random_item():
        random_item_num = randint(1, 8)
        if random_item_num == 1:
            random_item = "Apple"
            return random_item
        elif random_item_num == 2:
            random_item = "Potion"
            return random_item
        elif random_item_num == 3:
            random_item = "Iron Sword"
            return random_item
        elif random_item_num == 4:
            random_item = "Shield"
            return random_item
        elif random_item_num == 5:
            random_item = "Diamond"
            return random_item
        elif random_item_num == 6:
            random_item = "Bread"
            return random_item
        elif random_item_num == 7:
            random_item = "Wood"
            return random_item
        elif random_item_num == 8:
            random_item = "Gold Coin"
            return random_item

    random_item = find_random_item()
    if not random_item in inventory:
        print(f"✨ You explored the world and found {random_item}!")
        oformity1()
        print(f"➕ Item ({random_item}) add to inventory!")
        oformity1()
        inventory.append(random_item)
        return inventory
    elif random_item in inventory:
        print(f"✨ You explored the world and found {random_item}!")
        oformity1()
        print(f"❗ Item ({random_item}) can't be add to inventory, you have it!")
        oformity1()
        return inventory
    else:
        print(f"❗ Error!")
        oformity1()
        return inventory

def use_item(inventory, player_hp, player_gold):
    global shield_used
    def find_using_item(item_to_use):
        if item_to_use == "Apple":
            using_item = item_to_use.lower().strip()
            buff = 10
            return using_item, buff
        elif item_to_use == "Potion":
            using_item = item_to_use.lower().strip()
            buff = 20
            return using_item, buff
        elif item_to_use == "Iron Sword":
            using_item = item_to_use.lower().strip()
            buff = "Go_Fight"
            return using_item, buff
        elif item_to_use == "Shield":
            using_item = item_to_use.lower().strip()
            buff = True
            return using_item, buff
        elif item_to_use == "Diamond":
            using_item = item_to_use.lower().strip()
            buff = 100
            return using_item, buff
        elif item_to_use == "Bread":
            using_item = item_to_use.lower().strip()
            buff = 15
            return using_item, buff
        elif item_to_use == "Wood":
            using_item = item_to_use.lower().strip()
            buff = 50
            return using_item, buff
        elif item_to_use == "Gold Coin":
            using_item = item_to_use.lower().strip()
            buff = 75
            return using_item, buff
        else:
            using_item = "Error!"
            buff = None
            return using_item, buff

    def go_to_fight(player_hp, player_gold, shield_used):
        random_enemy_num = randint(0, 5)
        def find_enemy(random_enemy):
            if random_enemy == 0:
                enemy = "Goblin"
                enemy_attack = randint(1, 3)
                enemy_hp = randint(40, 80)
                return enemy, enemy_attack, enemy_hp
            elif random_enemy == 1:
                enemy = "Goblin king"
                enemy_attack = randint(2, 5)
                enemy_hp = randint(60, 100)
                return enemy, enemy_attack, enemy_hp
            elif random_enemy == 2:
                enemy = "Dirt Golem"
                enemy_attack = randint(3, 6)
                enemy_hp = randint(80, 120)
                return enemy, enemy_attack, enemy_hp
            elif random_enemy == 3:
                enemy = "Skeletons army"
                enemy_attack = randint(3, 7)
                enemy_hp = randint(100, 120)
                return enemy, enemy_attack, enemy_hp
            elif random_enemy == 4:
                enemy_attack = randint(5, 8)
                enemy = "Witch"
                enemy_hp = randint(100, 120)
                return enemy, enemy_attack, enemy_hp
            elif random_enemy == 5:
                enemy_attack = randint(6, 10)
                enemy = "Dragon"
                enemy_hp = randint(120, 160)
                return enemy, enemy_attack, enemy_hp
            else:
                enemy_attack = randint(10, 15)
                enemy = "Secret Error Enemy"
                enemy_hp = randint(150, 250)
                return enemy, enemy_attack, enemy_hp

        def check_enemy_dead(enemy_hp, player_gold):
            if enemy_hp <= 0:
                random_gold = randint(10, 50)
                print("💀 Enemy dead!")
                oformity1()
                print("🏆 You win!")
                oformity1()
                print(f"💰 Your reward is: {random_gold} gold!")
                oformity1()
                player_gold += random_gold
                enemy_dead = True
                return player_gold, enemy_dead
            else:
                enemy_dead = False
                return player_gold, enemy_dead
            
        enemy, enemy_damage, enemy_hp = find_enemy(random_enemy_num)

        if shield_used:
            shield_used = False
            shield_break = False
            while True:
                dead = check_dead(player_hp)
                if dead == True:
                    print("💀 You died!")
                    oformity1()
                    exit_game(inventory, player_hp, player_gold)
                    break
                player_damage = randint(5, 10)
                print(f"⚔️  Your enemy: {enemy}!")
                oformity1()
                print(f"❤️  {enemy} HP: {enemy_hp}")
                oformity2()
                print(f"❤️  Your HP: {player_hp}")
                oformity1()
                print("1️⃣  1. Attack")
                print("2️⃣  2. Run")
                oformity1()
                fight_choose = input("⌨️  Enter your choice: ").lower().strip()
                oformity1()
                if fight_choose.isdigit():
                    fight_choose = int(fight_choose)
                    if fight_choose == 1:
                        if shield_break == False:
                            print(f"⚔️  You attack {enemy}!")
                            oformity1()
                            print(f"⚔️  You hit {enemy}!")
                            oformity2()
                            print(f"💔  {enemy}: -{player_damage}HP!")
                            oformity1()
                            print(f"🛡️  {enemy} try to attack you, but shield defense you!")
                            oformity2()
                            print(f"🛡️  Shield broke!")
                            oformity1()
                            enemy_hp -= player_damage
                            shield_break = True
                            dead = check_dead(player_hp)
                            if dead == True:
                                print("💀 You died!")
                                oformity1()
                                exit_game(inventory, player_hp, player_gold)
                                break
                            player_gold, enemy_dead = check_enemy_dead(enemy_hp, player_gold)
                            if enemy_dead:
                                shield_used = False
                                return player_hp, player_gold, dead, shield_used
                            else:
                                continue
                        else:
                            print(f"⚔️  You attack {enemy}!")
                            oformity1()
                            print(f"⚔️  You hit {enemy}!")
                            oformity2()
                            print(f"💔  {enemy}: -{player_damage}HP!")
                            oformity1()
                            print(f"⚔️  Because of your shield broke {enemy} hit you!")
                            oformity2()
                            print(f"💔  You: -{enemy_damage}HP!")
                            oformity1()
                            player_hp -= enemy_damage
                            enemy_hp -= player_damage
                            dead = check_dead(player_hp)
                            if dead == True:
                                print("💀 You died!")
                                oformity1()
                                exit_game(inventory, player_hp, player_gold)
                                break
                            player_gold, enemy_dead = check_enemy_dead(enemy_hp, player_gold)
                            if enemy_dead:
                                shield_used = False
                                return player_hp, player_gold, dead, shield_used
                            else:
                                continue
                    elif fight_choose == 2:
                        if enemy == "Goblin" or enemy == "Goblin king":
                            print(f"🏃 You run from {enemy}...")
                            oformity1()
                            print(f"🏃 And you escaped successfully from {enemy}!")
                            oformity1()
                            dead = check_dead(player_hp)
                            break
                        elif enemy == "Dirt Golem" or enemy == "Skeletons army":
                            successfull_run = randint(0, 1)
                            print(f"🏃 You run from {enemy}...")
                            oformity1()
                            if successfull_run == 0:
                                print(f"🫳 But {enemy} grab you and go back to fighting area!")
                                oformity1()
                                dead = check_dead(player_hp)
                                continue
                            else:
                                print(f"🏃 And you escaped successfully from {enemy}!")
                                oformity1()
                                dead = check_dead(player_hp)
                                break
                        else:
                            print(f"🏃 You run from {enemy}...")
                            oformity1()
                            print(f"🏃 But {enemy} got angry and hit you!")
                            oformity1()
                            player_hp -= enemy_damage
                            dead = check_dead(player_hp)
                            if dead == True:
                                print("💀 You died!")
                                oformity1()
                                exit_game(inventory, player_hp, player_gold)
                                break
                            continue
                    else:
                        print("❗ Not right number of choice!")
                        oformity1()
                        continue
                elif fight_choose == "":
                    print("❗ Choice can't be empty!")
                    oformity1()
                    continue
                else:
                    print("❗ Choice need to be numbers!")
                    oformity1()
                    continue
        elif shield_used == False:
            while True:
                dead = check_dead(player_hp)
                if dead == True:
                    print("💀 You died!")
                    oformity1()
                    exit_game(inventory, player_hp, player_gold)
                    break
                player_damage = randint(5, 10)
                print(f"⚔️  Your enemy: {enemy}!")
                oformity1()
                print(f"❤️  {enemy} HP: {enemy_hp}")
                oformity2()
                print(f"❤️  Your HP: {player_hp}")
                oformity1()
                print("1️⃣  1. Attack")
                print("2️⃣  2. Run")
                oformity1()
                fight_choose = input("⌨️  Enter your choice: ").lower().strip()
                oformity1()
                if fight_choose.isdigit():
                    fight_choose = int(fight_choose)
                    if fight_choose == 1:
                        print(f"⚔️  You attack {enemy}!")
                        oformity1()
                        print(f"⚔️  You hit {enemy}!")
                        oformity2()
                        print(f"💔  {enemy}: -{player_damage}HP!")
                        oformity1()
                        print(f"⚔️  {enemy} hit you!")
                        oformity2()
                        print(f"💔  You: -{enemy_damage}HP!")
                        oformity1()
                        player_hp -= enemy_damage
                        enemy_hp -= player_damage
                        dead = check_dead(player_hp)
                        if dead == True:
                            print("💀 You died!")
                            oformity1()
                            exit_game(inventory, player_hp, player_gold)
                            break
                        player_gold, enemy_dead = check_enemy_dead(enemy_hp, player_gold)
                        if enemy_dead:
                            shield_used = False
                            return player_hp, player_gold, dead, shield_used
                        else:
                            continue
                    elif fight_choose == 2:
                        if enemy == "Goblin" or enemy == "Goblin king":
                            print(f"🏃 You run from {enemy}...")
                            oformity1()
                            print(f"🏃 And you escaped successfully from {enemy}!")
                            oformity1()
                            dead = check_dead(player_hp)
                            break
                        elif enemy == "Dirt Golem" or enemy == "Skeletons army":
                            successfull_run = randint(0, 1)
                            print(f"🏃 You run from {enemy}...")
                            oformity1()
                            if successfull_run == 0:
                                print(f"🫳 But {enemy} grab you and go back to fighting area!")
                                oformity1()
                                dead = check_dead(player_hp)
                                continue
                            else:
                                print(f"🏃 And you escaped successfully from {enemy}!")
                                oformity1()
                                dead = check_dead(player_hp)
                                break
                        else:
                            print(f"🏃 You run from {enemy}...")
                            oformity1()
                            print(f"🏃 But {enemy} got angry and hit you!")
                            oformity1()
                            player_hp -= enemy_damage
                            dead = check_dead(player_hp)
                            if dead == True:
                                print("💀 You died!")
                                oformity1()
                                exit_game(inventory, player_hp, player_gold)
                                break
                            continue
                    else:
                        print("❗ Not right number of choice!")
                        oformity1()
                        continue
                elif fight_choose == "":
                    print("❗ Choice can't be empty!")
                    oformity1()
                    continue
                else:
                    print("❗ Choice need to be numbers!")
                    oformity1()
                    continue
                
        dead = check_dead(player_hp)
        shield_used = False
        return player_hp, player_gold, dead, shield_used
    
    if not inventory:
        print("❗ Inventory is empty, no items to use!")
        oformity1()
        return inventory, player_hp, player_gold
    else:
        while True:
            print("🎒 Your inventory: ", end="")
            ryad = ""
            for item in inventory:
                ryad = ryad + item + "; "
            print(ryad[0: -2: 1])
            oformity1()
            user_use = input("⌨️  Enter name of item to use: ").lower().strip()
            oformity1()
            for item in inventory:
                item_new = item.strip().lower()
                if item_new == user_use:
                    item_to_use = item
                    break
                else:
                    item_to_use = False
                    continue
            if item_to_use == False:
                print("❗ Not right name of item!")
                oformity1()
            else:
                using_item, buff = find_using_item(item_to_use)
                if using_item == user_use and buff != None:
                    if using_item == "diamond" or using_item == "wood" or using_item == "gold coin":
                        player_gold += buff
                        print(f"💰 Item used! +{buff} gold!")
                        oformity1()
                        dead = check_dead(player_hp)
                    elif using_item != "diamond" and using_item != "wood" and using_item != "gold coin" and using_item != "iron sword" and using_item != "shield":
                        player_hp += buff
                        print(f"❤️  Item used! +{buff} HP!")
                        oformity1()
                        dead = check_dead(player_hp)
                    elif using_item == "iron sword":
                        print("⚔️  Item used! Going to fight!")
                        oformity1()
                        player_hp, player_gold, dead, shield_used = go_to_fight(player_hp, player_gold, shield_used)
                        oformity1()
                        return inventory, player_hp, player_gold, dead
                    elif using_item == "shield":
                        if shield_used == False:
                            print("🛡️  Item used! Shield for next fight!")
                            oformity1()
                            shield_used = True
                            dead = check_dead(player_hp)
                        elif shield_used:
                            print("❗ Shield alredy used!")
                            oformity1()
                            dead = check_dead(player_hp)
                            return inventory, player_hp, player_gold, dead
                    else:
                        print("❗ Error of buff!")
                        oformity1()
                        dead = check_dead(player_hp)
                    inventory.remove(item_to_use)
                    print("🎒 Item deleted from inventory!")
                    oformity1()
                    return inventory, player_hp, player_gold, dead
                else:
                    print("❗ Item or buff is none!")
                    oformity1()
                    continue
                
def show_stats(inventory, player_hp, player_gold):
    print("📊 Your stats:")
    oformity1()
    print(f"🎒 Items: {len(inventory)}")
    print(f"❤️  HP: {player_hp}")
    print(f"💰 Gold: {player_gold}")
    oformity1()

def exit_game(inventory, player_hp, player_gold):
    show_stats(inventory, player_hp, player_gold)
    print("👋 Goodbye!")
    exit()

print("👋 Welcome to the RPG!")
starter_time = time()
oformity1()
while True:
    print("=== RPG ===")
    oformity1()
    print("1️⃣  1. Show inventory")
    oformity2()
    print("2️⃣  2. Explore")
    oformity2()
    print("3️⃣  3. Use item")
    oformity2()
    print("4️⃣  4. Show stats")
    oformity2()
    print("5️⃣  5. Exit")
    oformity1()
    user_choice = input("⌨️  Enter your choice: ").strip()
    oformity1()
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice == 1:
            show_inventory(inventory)
        elif user_choice == 2:
            inventory = explore(inventory)
        elif user_choice == 3:
            inventory, player_hp, player_gold, dead = use_item(inventory, player_hp, player_gold)
            if dead == True:
                print("💀 You died!")
                oformity1()
                exit_game(inventory, player_hp, player_gold)
                break
        elif user_choice == 4:
            show_stats(inventory, player_hp, player_gold)
        elif user_choice == 5:
            exit_game(inventory, player_hp, player_gold)
            break
        else:
            print("❗ Not right number of choice!")
            oformity1()
            continue
    elif user_choice == "":
        print("❗ Choice can't be empty!")
        oformity1()
        continue
    elif user_choice.isalpha():
        print("❗ Choice need to be number!")
        oformity1()
        continue
    else:
        print("❗ Choice need to be number!")
        oformity1()
        continue
#Done
#v1.0
import time

monster_HP = 80

player_HP = 100

monster_Attack = 10

player_Attack = 15

iteration = 1

back_choose = ""

def attack(name, monster_HP, player_Attack, player_HP, monster_Attack):
    print(f"{name}, you attack!")
    print("The monster's HP decreased by 15!")
    time.sleep(0.5)
    monster_HP -= player_Attack
    print(" ")
    print("Monster attack too!")
    print("Your HP decreased by 10!")
    player_HP -= monster_Attack
    time.sleep(0.5)
    print(" ")
    print(f"{name} HP - {player_HP} | Monster HP - {monster_HP}")
    return player_HP, monster_HP

def defense(name, player_HP, monster_HP):
    print(f"{name} you defense attack of the monster! But he is very strong!")
    print(" ")
    time.sleep(0.5)
    print("Your HP is decreased by 5!")
    print(" ")
    player_HP -= 5
    time.sleep(0.5)
    print("You attacking from shield! Monster HP is decreased by 5!")
    monster_HP -= 5
    print(" ")
    print(f"{name} HP - {player_HP} | Monster HP - {monster_HP}")
    time.sleep(0.5)
    return player_HP, monster_HP

def run(name, it, player_HP, monster_HP):
    print(f"{name}, you are try run!")
    print(" ")
    time.sleep(0.5)
    if it > 2:
        print("You are running with all your might.")
        print(" ")
        time.sleep(0.5)
        print("You managed to get away!")
        return player_HP, monster_HP
    else:
        print("You are running with all your might.")
        print(" ")
        print("You didn't manage to escape from the monster!")
        time.sleep(0.5)
        print(" ")
        print("Your HP is decreased by 20!")
        player_HP -= 20
        time.sleep(0.5)
        print(" ")
        print(f"{name} HP - {player_HP} | Monster HP - {monster_HP}")
        print(" ")
        return player_HP, monster_HP

print("=== Battle Arena Simulator ===")
print(" ")
time.sleep(0.5)
while True:
    if player_HP <= 0:
        print("You die!")
        break
    elif monster_HP <= 0:
        print("You kill the monster!")
        break

    if iteration == 1:
        name_player = input("Enter your name to start battle with monster: ").capitalize()
        time.sleep(0.5)
        print("Battle start!")
        print(" ")
        time.sleep(0.5)
    iteration += 1

    print(" ")
    time.sleep(0.5)
    if back_choose != "a":
        print(f"{name_player} HP - {player_HP} | Monster HP - {monster_HP}")
        print(" ")
    time.sleep(0.5)
    
    
    print("Choose what to do:")
    time.sleep(0.5)
    print("1. Attack monster!")
    time.sleep(0.5)
    print("2. Defense from attack of the monster!")
    time.sleep(0.5)
    print("3. Run away!")
    time.sleep(0.5)
    print(" ")
    choose = int(input("Choose what you want do: "))
    print(" ")

    if choose == 1:
        time.sleep(0.5)
        player_HP, monster_HP = attack(name_player, monster_HP, player_Attack, player_HP, monster_Attack)
        back_choose = "a"
        print(" ")
        if monster_HP <= 0:
            print("You kill the monster!")
            break
        else:
            continue
    elif choose == 2:
        time.sleep(0.5)
        player_HP, monster_HP = defense(name_player, player_HP, monster_HP)
        back_choose = "a"
        print(" ")
        continue
    elif choose == 3:
        if monster_HP <= 0:
            print("You kill the monster!")
            break
        else:
            time.sleep(0.5)
            player_HP, monster_HP = run(name_player, iteration, player_HP, monster_HP)
            back_choose = "a"
            if iteration > 2:
                break
            continue
    else:
        time.sleep(0.5)
        print("Not right choose!")      
        continue
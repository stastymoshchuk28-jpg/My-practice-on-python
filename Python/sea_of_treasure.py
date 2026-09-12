from turtle import *
from random import choice, randint
from time import sleep
speed(0)
coordinates = []
bgcolor("khaki")
tracer(0)

def start(x, y):
    penup()
    goto(x, y)
    pendown()

def pause_long():
    print(" ")
    sleep(0.5)

def pause_short():
    sleep(0.1)

def generate_sea(coordinates:list, size:int, col_sea:str, width_sea_pixel:int, x_coord:tuple, y_coord:tuple, max_traps:int):
    def generate_coordinates(coordinates, size, x_s, x_e, y_s, y_e):
        for y in range(y_s, y_e, size):
            for x in range(x_s, x_e, size):
                coord = {"coordinate": (x, y), "entity": "water"}
                coordinates.append(coord)
        return coordinates
    coordinates = generate_coordinates(coordinates, size, x_coord[0], x_coord[1], y_coord[0], y_coord[1])

    def draw_sea(coordinates, size, col, wid):
        width(wid)
        color(col)
        for coord in coordinates:
            x, y = coord["coordinate"][0], coord["coordinate"][1]
            start(x, y)
            begin_fill()
            for line in range(0, 4, 1):
                fd(size)
                rt(90)
            end_fill()
    draw_sea(coordinates, size, col_sea, width_sea_pixel)

    def treasure_and_traps(coordinates, max_traps, size):
        seth(0)

        storms = 0
        pirates_attacks = 0
        while max_traps > 0:
            traps_type = ["storm", "pirates_attack"]
            if pirates_attacks < 1 and storms > 0:
                type_of_trap = "pirates_attack"
            elif pirates_attacks > 0 and storms < 1:
                type_of_trap = "storm"
            else:
                type_of_trap = choice(traps_type)
            coor = choice(coordinates)
            
            if coor["entity"] == "water":
                coor["entity"] = type_of_trap
                x, y = coor["coordinate"][0], coor["coordinate"][1]
                start(x+size/2, y-size/2)
                if type_of_trap == "storm":
                    color("slategray")
                else:
                    color("darkgoldenrod")
                begin_fill()
                for line in range(0, 4, 1):
                    fd(size)
                    rt(90)
                end_fill()
                max_traps -= 1
            else:
                continue
        while True:
            coor = choice(coordinates)
            if coor["entity"] == "water":
                coor["entity"] = "treasure"
                x, y = coor["coordinate"][0], coor["coordinate"][1]
                break
        return coordinates

    coordinates = treasure_and_traps(coordinates, max_traps, size-10)
    return coordinates

def spawn_player(coordinates:list, size_for_pixel:int):
    def find_neigbors(coord:dict, coordinates:list, size_for_pixel:int):
        x, y = coord["coordinate"][0], coord["coordinate"][1]

        coords_to_find = {
            "up": (x, y-size_for_pixel),
            "down": (x, y+size_for_pixel),
            "left": (x-size_for_pixel, y),
            "rigth": (x+size_for_pixel, y)
        }
        coord_up_found = False
        coord_down_found = False
        coord_left_found = False
        coord_rigth_found = False
        for c in coordinates:
            coordinates_of_coor = c["coordinate"]
            if coordinates_of_coor == coords_to_find["up"] and not coord_up_found and c["entity"] == "water":
                coord_up_found = True
            elif coordinates_of_coor == coords_to_find["down"] and not coord_down_found and c["entity"] == "water":
                coord_down_found = True
            elif coordinates_of_coor == coords_to_find["left"] and not coord_left_found and c["entity"] == "water":
                coord_left_found = True
            elif coordinates_of_coor == coords_to_find["rigth"] and not coord_rigth_found and c["entity"] == "water":
                coord_rigth_found = True
            else:
                continue
        if coord_up_found and coord_down_found and coord_left_found and coord_rigth_found:
            return True
        else:
            return False
        
    last_index_pos = None
    for coord_index, coord in enumerate(coordinates, start=0):
        if coord["entity"] == "water":
            neigbors_found = find_neigbors(coord, coordinates, size_for_pixel)
            if neigbors_found:
                pencolor("black")
                fillcolor("brown")
                seth(0)
                start(coord["coordinate"][0]+size_for_pixel/2, coord["coordinate"][1]-size_for_pixel/2)
                coord["entity"] = "player"
                last_index_pos = coord_index
                break
    return coordinates, last_index_pos

def move_player(command:str, coordinates:list, last_pos_index_player:int, size_for_pixel:int, fuel:int, hp:int, win:bool, lose:bool):
    def check_entity_and_do_action(entity_of_next_cell:str, fuel:int, hp:int, win:bool, lose:bool):
        def check_next_cell_entity(entity_of_next_cell:str):
            if entity_of_next_cell == "water":
                return False, False, False, True
            elif entity_of_next_cell == "storm":
                return False, True, False, False
            elif entity_of_next_cell == "pirates_attack":
                return False, False, True, False
            elif entity_of_next_cell == "treasure":
                return True, False, False, False
            
        found_treasure, trap_storm, trap_pirates, water = check_next_cell_entity(entity_of_next_cell)
        if found_treasure and hp > 0 and fuel > 0:
            print("✨💰 You found a treasure!")
            pause_long()
            print("🏆✨ You win!")
            win = True
            return fuel, hp, win, lose
        elif found_treasure and hp <= 0:
            print("✨💰 You found a treasure!")
            pause_long()
            print("🏆❌ But you don't win!")
            pause_long()
            print("💔 You dead!")
            pause_long()             
            lose = True
            return fuel, hp, win, lose
        elif found_treasure and fuel <= 0:
            print("✨💰 You found a treasure!")
            pause_long()
            print("🏆❌ But you don't win!")
            pause_long()
            print("⛽ The fuel ran out! The ship was lost at sea forever.")
            pause_long() 
            lose = True
            return fuel, hp, win, lose
        elif trap_storm:
            minus_fuel = randint(1, 3)
            minus_hp = randint(1, 5)
            print("🌪️  Oh no! Storm!")
            pause_long()
            fuel -= minus_fuel
            hp -= minus_hp
            print(f"⛽❤️  Now you have:\n•HP: {hp};\nFuel: {fuel}")
            pause_long()
            if hp <= 0:
                print("💔 You dead!")
                lose = True
            elif fuel <= 0:
                print("⛽ The fuel ran out! The ship was lost at sea forever.")
                lose = True
            return fuel, hp, win, lose
        elif trap_pirates:
            minus_fuel = randint(1, 5)
            minus_hp = randint(1, 4)
            print("🚢🏴‍☠️ Oh no! Pirates attack!")
            pause_long()
            fuel -= minus_fuel
            hp -= minus_hp
            print(f"⛽❤️ Now you have:\n•HP: {hp};\nFuel: {fuel}")
            pause_long()
            if hp <= 0:
                print("💔 You dead!")
                lose = True
            elif fuel <= 0:
                print("⛽ The fuel ran out! The ship was lost at sea forever.")
                lose = True
            return fuel, hp, win, lose
        elif water:
            fuel -= 1
            if hp <= 0:
                print("💔 You dead!")
                lose = True
            elif fuel <= 0:
                print("⛽ The fuel ran out! The ship was lost at sea forever.")
                lose = True
            return fuel, hp, win, lose

    def get_hint(coordinates:list, last_pos_index_player:int, next_coords:tuple):
        for treasure_coords in coordinates:
            if treasure_coords["entity"] == "treasure":
                break
        last_coords_player = list(coordinates[last_pos_index_player]["coordinate"])
        coords_of_treasure = list(treasure_coords["coordinate"])
        next_coords = list(next_coords)
        if abs(last_coords_player[0] - coords_of_treasure[0]) < abs(next_coords[0] - coords_of_treasure[0]):
            print("❄️ Colder!")
            pause_long()
        elif abs(last_coords_player[1] - coords_of_treasure[1]) < abs(next_coords[1] - coords_of_treasure[1]):
            print("❄️ Colder!")
            pause_long()
        elif abs(last_coords_player[0] - coords_of_treasure[0]) > abs(next_coords[0] - coords_of_treasure[0]):
            print("🔥 Getting warmer!!")
            pause_long()
        elif abs(last_coords_player[1] - coords_of_treasure[1]) > abs(next_coords[1] - coords_of_treasure[1]):
            print("🔥 Getting warmer!!")
            pause_long()
        else:
            print("🔥❌❄️❌ No changes!")
            pause_long()

    if command == "up":
        coords = coordinates[last_pos_index_player]
        x_of_player, y_of_player = coords["coordinate"][0], coords["coordinate"][1]
        next_coords_for_player = (x_of_player, y_of_player+size_for_pixel)
        found_cell_to_move = False
        for index_of_next_coords, next_coords in enumerate(coordinates, start=0):
            if next_coords["coordinate"] == next_coords_for_player:
                found_cell_to_move = True
                break
        if found_cell_to_move:
            next_coords = coordinates[index_of_next_coords]
            the_next_cell_entity = next_coords["entity"]
            fuel, hp, win, lose = check_entity_and_do_action(the_next_cell_entity, fuel, hp, win, lose)
            if the_next_cell_entity == "storm" or the_next_cell_entity == "pirates_attack":
                def kick_trap(next_coords, size):
                    start(next_coords["coordinate"][0], next_coords["coordinate"][1])
                    color("lightskyblue")
                    begin_fill()
                    for line in range(0, 4, 1):
                        fd(size)
                        rt(90)
                    end_fill()
                    pencolor("black")
                    fillcolor("brown")
                coords["entity"] = "water"
                seth(0)
                kick_trap(next_coords, size_for_pixel)
                start(next_coords["coordinate"][0]+size_for_pixel/2, next_coords["coordinate"][1]-size_for_pixel/2)
                if not win and not lose:
                    get_hint(coordinates, last_pos_index_player, next_coords_for_player)
                last_pos_index_player = index_of_next_coords
            elif the_next_cell_entity == "treasure":
                def win_text():
                    color("red")
                    start(-100, 100)
                    write("You win", font=("Arial", 20))
                    pencolor("black")
                    fillcolor("brown")
                coords["entity"] = "water"
                seth(0)
                win_text()
                start(next_coords["coordinate"][0]+size_for_pixel/2, next_coords["coordinate"][1]-size_for_pixel/2)
                if not win and not lose:
                    get_hint(coordinates, last_pos_index_player, next_coords_for_player)
                last_pos_index_player = index_of_next_coords                
            else:
                coords["entity"] = "water"
                seth(90)
                start(next_coords["coordinate"][0]+size_for_pixel/2, next_coords["coordinate"][1]-size_for_pixel/2)
                next_coords["entity"] = "player"
                if not win and not lose:
                    get_hint(coordinates, last_pos_index_player, next_coords_for_player)
                last_pos_index_player = index_of_next_coords
        else:
            print("❗ You are at the edge of the sea - you cannot swim there!")
            pause_long()
    elif command == "down":
        coords = coordinates[last_pos_index_player]
        x_of_player, y_of_player = coords["coordinate"][0], coords["coordinate"][1]
        next_coords_for_player = (x_of_player, y_of_player-size_for_pixel)
        found_cell_to_move = False
        for index_of_next_coords, next_coords in enumerate(coordinates, start=0):
            if next_coords["coordinate"] == next_coords_for_player:
                found_cell_to_move = True
                break
        if found_cell_to_move:
            next_coords = coordinates[index_of_next_coords]
            the_next_cell_entity = next_coords["entity"]
            fuel, hp, win, lose = check_entity_and_do_action(the_next_cell_entity, fuel, hp, win, lose)
            if the_next_cell_entity == "storm" or the_next_cell_entity == "pirates_attack":
                def kick_trap(next_coords, size):
                    start(next_coords["coordinate"][0], next_coords["coordinate"][1])
                    color("lightskyblue")
                    begin_fill()
                    for line in range(0, 4, 1):
                        fd(size)
                        rt(90)
                    end_fill()
                    pencolor("black")
                    fillcolor("brown")
                coords["entity"] = "water"
                seth(0)
                kick_trap(next_coords, size_for_pixel)
                seth(270)
                start(next_coords["coordinate"][0]+size_for_pixel/2, next_coords["coordinate"][1]-size_for_pixel/2)
                if not win and not lose:
                    get_hint(coordinates, last_pos_index_player, next_coords_for_player)
                last_pos_index_player = index_of_next_coords
            elif the_next_cell_entity == "treasure":
                def win_text():
                    color("red")
                    start(-100, 100)
                    write("You win", font=("Arial", 20))
                    pencolor("black")
                    fillcolor("brown")
                coords["entity"] = "water"
                seth(0)
                win_text()
                seth(270)
                start(next_coords["coordinate"][0]+size_for_pixel/2, next_coords["coordinate"][1]-size_for_pixel/2)
                if not win and not lose:
                    get_hint(coordinates, last_pos_index_player, next_coords_for_player)
                last_pos_index_player = index_of_next_coords                
            else:
                coords["entity"] = "water"
                seth(270)
                start(next_coords["coordinate"][0]+size_for_pixel/2, next_coords["coordinate"][1]-size_for_pixel/2)
                next_coords["entity"] = "player"
                if not win and not lose:
                    get_hint(coordinates, last_pos_index_player, next_coords_for_player)
                last_pos_index_player = index_of_next_coords  
        else:
            print("❗ You are at the edge of the sea - you cannot swim there!")
            pause_long()       
    elif command == "rigth":
        coords = coordinates[last_pos_index_player]
        x_of_player, y_of_player = coords["coordinate"][0], coords["coordinate"][1]
        next_coords_for_player = (x_of_player+size_for_pixel, y_of_player)
        found_cell_to_move = False
        for index_of_next_coords, next_coords in enumerate(coordinates, start=0):
            if next_coords["coordinate"] == next_coords_for_player:
                found_cell_to_move = True
                break
        if found_cell_to_move:
            next_coords = coordinates[index_of_next_coords]
            the_next_cell_entity = next_coords["entity"]
            fuel, hp, win, lose = check_entity_and_do_action(the_next_cell_entity, fuel, hp, win, lose)
            if the_next_cell_entity == "storm" or the_next_cell_entity == "pirates_attack":
                def kick_trap(next_coords, size):
                    start(next_coords["coordinate"][0], next_coords["coordinate"][1])
                    color("lightskyblue")
                    begin_fill()
                    for line in range(0, 4, 1):
                        fd(size)
                        rt(90)
                    end_fill()
                    pencolor("black")
                    fillcolor("brown")
                coords["entity"] = "water"
                seth(0)
                kick_trap(next_coords, size_for_pixel)
                seth(0)
                start(next_coords["coordinate"][0]+size_for_pixel/2, next_coords["coordinate"][1]-size_for_pixel/2)
                if not win and not lose:
                    get_hint(coordinates, last_pos_index_player, next_coords_for_player)
                last_pos_index_player = index_of_next_coords
            elif the_next_cell_entity == "treasure":
                def win_text():
                    color("red")
                    start(-100, 100)
                    write("You win", font=("Arial", 20))
                    pencolor("black")
                    fillcolor("brown")
                coords["entity"] = "water"
                seth(0)
                win_text()
                seth(0)
                start(next_coords["coordinate"][0]+size_for_pixel/2, next_coords["coordinate"][1]-size_for_pixel/2)
                if not win and not lose:
                    get_hint(coordinates, last_pos_index_player, next_coords_for_player)
                last_pos_index_player = index_of_next_coords                
            else:
                coords["entity"] = "water"
                seth(0)
                start(next_coords["coordinate"][0]+size_for_pixel/2, next_coords["coordinate"][1]-size_for_pixel/2)
                next_coords["entity"] = "player"
                if not win and not lose:
                    get_hint(coordinates, last_pos_index_player, next_coords_for_player)
                last_pos_index_player = index_of_next_coords
        else:
            print("❗ You are at the edge of the sea - you cannot swim there!")
            pause_long()
    elif command == "left":
        coords = coordinates[last_pos_index_player]
        x_of_player, y_of_player = coords["coordinate"][0], coords["coordinate"][1]
        next_coords_for_player = (x_of_player-size_for_pixel, y_of_player)
        found_cell_to_move = False
        for index_of_next_coords, next_coords in enumerate(coordinates, start=0):
            if next_coords["coordinate"] == next_coords_for_player:
                found_cell_to_move = True
                break
        if found_cell_to_move:
            next_coords = coordinates[index_of_next_coords]
            the_next_cell_entity = next_coords["entity"]
            fuel, hp, win, lose = check_entity_and_do_action(the_next_cell_entity, fuel, hp, win, lose)
            if the_next_cell_entity == "storm" or the_next_cell_entity == "pirates_attack":
                def kick_trap(next_coords, size):
                    start(next_coords["coordinate"][0], next_coords["coordinate"][1])
                    color("lightskyblue")
                    begin_fill()
                    for line in range(0, 4, 1):
                        fd(size)
                        rt(90)
                    end_fill()
                    pencolor("black")
                    fillcolor("brown")
                coords["entity"] = "water"
                seth(0)
                kick_trap(next_coords, size_for_pixel)
                seth(180)
                start(next_coords["coordinate"][0]+size_for_pixel/2, next_coords["coordinate"][1]-size_for_pixel/2)
                if not win and not lose:
                    get_hint(coordinates, last_pos_index_player, next_coords_for_player)
                last_pos_index_player = index_of_next_coords
            elif the_next_cell_entity == "treasure":
                def win_text():
                    color("red")
                    start(-100, 100)
                    write("You win", font=("Arial", 20))
                    pencolor("black")
                    fillcolor("brown")
                coords["entity"] = "water"
                seth(0)
                win_text()
                seth(180)
                start(next_coords["coordinate"][0]+size_for_pixel/2, next_coords["coordinate"][1]-size_for_pixel/2)
                if not win and not lose:
                    get_hint(coordinates, last_pos_index_player, next_coords_for_player)
                last_pos_index_player = index_of_next_coords                
            else:
                coords["entity"] = "water"
                seth(180)
                start(next_coords["coordinate"][0]+size_for_pixel/2, next_coords["coordinate"][1]-size_for_pixel/2)
                next_coords["entity"] = "player"
                if not win and not lose:
                    get_hint(coordinates, last_pos_index_player, next_coords_for_player)
                last_pos_index_player = index_of_next_coords
        else:
            print("❗ You are at the edge of the sea - you cannot swim there!")
            pause_long()
    update()
    if lose:
        sleep(2.5)
    elif win:
        sleep(2.5)
    return coordinates, last_pos_index_player, fuel, hp, win, lose

def stop_game():
    print("✨ Thank you for playing 'Sea of treasure'!")
    pause_long()
    print("👋 Goodbye!")
    pause_long()

def game(coordinates:list, size_for_pixel:int, col_sea:str, width_sea_pixel:int, x_coord:tuple, y_coord:tuple, max_traps:int):
    commands = [
        "up",
        "down",
        "left",
        "rigth",       
        "exit"
    ]
    coordinates = generate_sea(coordinates, size_for_pixel, col_sea, width_sea_pixel, x_coord, y_coord, max_traps)
    coordinates, last_pos_index_player = spawn_player(coordinates, size_for_pixel)
    fuel = 50
    hp = 10
    win = False
    lose = False

    while True:
        update()
        print("=== Sea of treasure! ===")
        pause_short()
        print("💰 Find the hidden gold before you run out of fuel!")
        pause_long()
        print(f"Fuel: {fuel} | HP: {hp}")
        pause_long()
        move = input("🚶 Where to move? (up / down / left / rigth / exit): ").strip().lower()
        pause_long()
        if move in commands:
            if move == "up":
                coordinates, last_pos_index_player, fuel, hp, win, lose = move_player(move, coordinates, last_pos_index_player, size_for_pixel, fuel, hp, win, lose)
                if win:
                    break
                elif lose:
                    break
                else:
                    continue
            elif move == "down":
                coordinates, last_pos_index_player, fuel, hp, win, lose = move_player(move, coordinates, last_pos_index_player, size_for_pixel, fuel, hp, win, lose)
                if win:
                    break
                elif lose:
                    break
                else:
                    continue
            elif move == "left":
                coordinates, last_pos_index_player, fuel, hp, win, lose = move_player(move, coordinates, last_pos_index_player, size_for_pixel, fuel, hp, win, lose)
                if win:
                    break
                elif lose:
                    break
                else:
                    continue
            elif move == "rigth":
                coordinates, last_pos_index_player, fuel, hp, win, lose = move_player(move, coordinates, last_pos_index_player, size_for_pixel, fuel, hp, win, lose)
                if win:
                    break
                elif lose:
                    break
                else:
                    continue
            elif move == "exit":
                stop_game()
                break         
        else:
            print("❗ Enter right command! List of command: up / down / left / rigth / exit.")
            pause_long()

game(coordinates, 20, "lightskyblue", 5, (-100, 101), (-100, 101), 10)
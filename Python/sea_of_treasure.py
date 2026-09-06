from turtle import *
from random import choice
from time import sleep
speed(0)
coordinates = []
bgcolor("khaki")

def start(x, y):
    penup()
    goto(x, y)
    pendown()

def generate_sea(coordinates:list, size:int, col_sea:str, width_sea_pixel:int, x_coord:tuple, y_coord:tuple, max_traps:int):
    def generate_coordinates(coordinates, size, x_s, x_e, y_s, y_e):
        for y in range(y_s, y_e, size):
            for x in range(x_s, x_e, size):
                coord = {"coordinate": (x, y), "entity": "water"}
                coordinates.append(coord)
        return coordinates
    coordinates = generate_coordinates(coordinates, size, x_coord[0], x_coord[1], y_coord[0], y_coord[1])

    def draw_sea(coordinates, size, col, wid):
        x_start = coordinates[0]["coordinate"][0]
        x_end = coordinates[120]["coordinate"][0]
        y_start = coordinates[0]["coordinate"][1]
        y_end = coordinates[120]["coordinate"][1]
        width(wid)
        color(col)
        for y in range(y_start, y_end, size):
            for x in range(x_start, x_end, size):
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
                start(x, y)
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
    print(coordinates)

generate_sea(coordinates, 20, "lightskyblue", 5, (-100, 101), (-100, 101), 10)
done()
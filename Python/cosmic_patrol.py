#Texts on ukrainian language
from turtle import *
from random import randint, choice
screen = getscreen()
screen.tracer(0)
screen.bgcolor("black")
hideturtle()
screen.update()

class SpaceObject(Turtle):
    def __init__(self, x, y, move_speed_x, move_speed_y, active=True):
        super().__init__()
        self.penup()
        self.goto(x, y)
        self.move_speed_x = move_speed_x
        self.move_speed_y = move_speed_y
        self.active = active

    def update(self):
        if self.active:
            self.move(self.move_speed_x, self.move_speed_y)

    def move(self, dx, dy):
        if self.active:
            now_x = self.xcor()
            now_y = self.ycor()
            next_x = now_x + dx
            next_y = now_y + dy
            self.goto(next_x, next_y)

    def destroy(self):
        self.active = False
        self.hideturtle()

class Projectile(SpaceObject):
    def __init__(self, x, y, move_speed_y, field_info, projectile_damage = 1, projectile_shape="square", projectile_color="red", size_wid=1, size_len=1, active=True):
        super().__init__(x, y, 0, move_speed_y, active)
        self.shape(projectile_shape)
        self.color(projectile_color)
        self.shapesize(stretch_wid=size_wid, stretch_len=size_len)
        self.seth(90)
        self.penup()
        self.size = size_len
        self.damage = projectile_damage
        self.field_info = field_info

    def update(self):
        super().update()
        y = self.ycor()
        if y+(10*self.size) >= self.field_info[0][1]:
            self.destroy()
        return None

class Weapon:
    def __init__(self, field_info, ammo=None, reloading_speed=2000, move_speed_y=2, weapon_damage=1, weapon_shape="square", weapon_color="red", size_wid=1, size_len=1, active=True):
        self.projectile_data = {"Shape": weapon_shape, "Color": weapon_color, "Damage": weapon_damage, "Size_wid": size_wid, "Size_len": size_len, "active": active}
        self.ammo = ammo
        self.reloading_speed = reloading_speed
        self.reloading_timer = reloading_speed
        self.move_speed = move_speed_y
        self.field_info = field_info

    def shoot(self, x_to_shoot, y_to_shoot):
            if self.ammo is None:
                if self.reloading_timer >= self.reloading_speed:
                    projectile = Projectile(x_to_shoot, y_to_shoot, self.move_speed, self.field_info, self.projectile_data["Damage"], self.projectile_data["Shape"], self.projectile_data["Color"], self.projectile_data["Size_wid"], self.projectile_data["Size_len"], self.projectile_data["active"])
                    self.reloading_timer = 0
                    return projectile
                else:
                    print(" ")
                    print("\nПерезарядка!\n")    
                return None
            else:
                if self.ammo > 0:
                    if self.reloading_timer >= self.reloading_speed:
                        projectile = Projectile(x_to_shoot, y_to_shoot, self.move_speed, self.field_info, self.projectile_data["Damage"], self.projectile_data["Shape"], self.projectile_data["Color"], self.projectile_data["Size_wid"], self.projectile_data["Size_len"], self.projectile_data["active"])
                        self.ammo -= 1
                        self.reloading_timer = 0
                        return projectile
                    else:
                        print(" ")
                        print("\nПерезарядка!\n")    
                else:
                    print(" ")
                    print("\nРакети закінчились!\n")
                return None

class Shield(SpaceObject):
    def __init__(self, x, y, shield_color, health, max_health):
        super().__init__(x, y, 0, 0, True)
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=1.75, stretch_len=1.75)
        self.color(shield_color)
        self.health = health
        self.max_health = max_health
        self.shield_color = shield_color

    def take_damage(self, damage=1):
        if self.health > 0:
            self.health -= damage
            if self.health < 0:
                self.health = 0
        if self.health <= 0:
            self.color("black")
        else:
            self.color(self.shield_color)

    def restore(self):
        self.health = self.max_health
        self.color(self.shield_color)

class SpaceShip(SpaceObject):
    def __init__(self, x, y, field_info, LaserLauncher, RocketLauncher, space_ship_color="lightgray", shield_color="Green", shield_max_health=3, active=True):
        shield = Shield(x, y, shield_color, shield_max_health, shield_max_health)
        super().__init__(x, y, 0, 0, active)
        self.shape("triangle")
        self.color(space_ship_color)
        self.seth(90)
        self.move_speed = 5
        self.field_info = field_info
        self.shield = shield
        self.weapons = {"Лазер": LaserLauncher, 
                        "Ракета": RocketLauncher}
        self.weapon_equiped = "Лазер"
        self.weapon_changer = Turtle()
        self.weapon_changer.penup()
        self.weapon_changer.color("royalblue")
        self.weapon_changer.shape("arrow")
        self.weapon_changer.goto(field_info[1][0]+25, field_info[1][1]-50)
        self.weapon_changer.onclick(self.change_weapon)
        self.getscreen().onkey(self.move_left, "Left")
        self.getscreen().onkey(self.move_right, "Right")
        self.getscreen().listen()

    def change_weapon(self, x, y):
        weapons_can_be = ("Лазер", "Ракета")
        if self.weapon_equiped == weapons_can_be[0]:
            self.weapon_equiped = weapons_can_be[1]
        else:
            self.weapon_equiped = weapons_can_be[0]

    def shoot(self):
        if self.active:
            x, y = self.xcor(), self.ycor()
            launcher = self.weapons[self.weapon_equiped]
            projectile = launcher.shoot(x, y)
            if projectile is not None:
                return projectile
            else:
                return None
    
    def move_left(self):
        x = self.xcor()
        if self.field_info[0][0]+20 <= x-self.move_speed <= self.field_info[1][0]-20:
            self.move(-self.move_speed, 0)
            self.shield.goto(self.xcor(), self.ycor())
        else:
            print("Гравець, ви не можете вийти за межі поля!\n")
        self.getscreen().update()   

    def move_right(self):
        x = self.xcor()
        if self.field_info[0][0]+20 <= x+self.move_speed <= self.field_info[1][0]-20:
            self.move(self.move_speed, 0)
            self.shield.goto(self.xcor(), self.ycor())
        else:
            print("Гравець, ви не можете вийти за межі поля!\n")
        self.getscreen().update()      

    def destroy(self):
        self.active = False
        self.hideturtle()
        self.shield.destroy()
        self.weapon_changer.hideturtle()

class Asteroid(SpaceObject):
    def __init__(self, x, y, field_info, move_speed=-2, asteroid_color="gray", size=1, damage=1, active=True):
        super().__init__(x, y, 0, move_speed, active)
        self.shape("circle")
        self.color(asteroid_color)
        self.shapesize(stretch_wid=size, stretch_len=size)
        self.seth(270)
        self.health_to_delete = 3
        self.field_info = field_info
        self.size = size
        self.damage = damage

    def update(self):
        super().update()
        y = self.ycor()
        if y-(10*self.size) <= self.field_info[2][1]:
            self.destroy()
        return None

class EnemyShip(SpaceObject):
    def __init__(self, x, y, field_info, move_speed_x=0, move_speed_y=-2, space_ship_color="slategray", space_ship_shape="triangle", size=1, damage=2, active=True):
        super().__init__(x, y, move_speed_x, move_speed_y, active)
        self.color(space_ship_color)
        self.shape(space_ship_shape)
        self.shapesize(stretch_wid=size, stretch_len=size)
        self.seth(270)
        self.health_to_delete = 3
        self.field_info = field_info
        self.damage = damage
        self.size = size

    def update(self):
        if self.active:
            super().update()
            y = self.ycor()
            if y-(10*self.size) <= self.field_info[2][1]:
                self.destroy()
                return -25
            return None

class Bonus(SpaceObject):
    def __init__(self, x, y, field_info, move_speed=-2, bonus_color="yellow", size=1, active=True):
        super().__init__(x, y, 0, move_speed, active)
        self.shapesize(stretch_wid=size, stretch_len=size)
        self.shape("circle")
        self.color(bonus_color)
        self.seth(270)
        self.penup()
        self.field_info = field_info
        self.size = size

    def update(self):
        super().update()
        y = self.ycor()
        if y-(10*self.size) <= self.field_info[2][1]:
            self.destroy()
        return None

    def apply_effect(self, game_data):
        print("Ефект бонуса активовано!")

class ShieldBonus(Bonus):
    def apply_effect(self, game_data):
        if game_data["player"].shield.health >= game_data["player"].shield.max_health:
            print(" ")
            print("\nЩит має максимальне здоров'я! Збільшити неможливо!\n")
        else:
            game_data["player"].shield.restore()
            print(" ")
            print(f"\nБонус підібрано: щит відновлено!\n")

class ScoreBonus(Bonus):
    def __init__(self, x, y, field_info, move_speed=-2, bonus_color="yellow", size=1, score_bonus=50, active=True):
        super().__init__(x, y, field_info, move_speed, bonus_color, size, active)
        self.score_bonus = score_bonus

    def apply_effect(self, game_data):
        game_data["score"] += self.score_bonus
        print(" ")
        print(f"\nБонус підібрано: очок +{self.score_bonus}!\n")

class Game:
    def __init__(self, field_info, for_game_UI):
        print("=== КОСМІЧНИЙ ПАТРУЛЬ ===\nЗахисти станцію від астероїдів і ворожих кораблів!\nСпочатку клікни по полотну і потім керуй! 1Керування: ← → рух, ПРОБІЛ постріл, клік по кнопці змінює зброю.\n")
        self.__game_data = {
            "game_going": True,
            "score": 0,
            "field_info": field_info,
            "asteroid_spawn_timer": 0,
            "asteroid_spawn_interval": 1500,
            "bonus_spawn_timer": 0,
            "bonus_spawn_interval": 5000,
            "enemy_spaceship_spawn_timer": 0,
            "enemy_spaceship_spawn_interval": 2500,
            "UI_texts": for_game_UI,
        }
        Laser_Launcher = Weapon(self.__game_data["field_info"], None, 500, 2, 1.5, "square", "red", 0.5, 1, True)
        Rocket_Launcher = Weapon(self.__game_data["field_info"], 10, 2500, 4, 3, "square", "darkorange", 1.5, 2, True)
        player = SpaceShip((self.__game_data["field_info"][0][0] + self.__game_data["field_info"][1][0])/2, self.__game_data["field_info"][2][1]+25, self.__game_data["field_info"], Laser_Launcher, Rocket_Launcher, "lightgray", "Green", 3, True)
        self.__game_data["player"] = player
        self.__game_data["objects"] = [player]
        self.__T = Turtle()
        self.__T.hideturtle()
        self.__T.penup()
        self.__T.color("white")
        self.field()
        self.__GameUI = Turtle()
        self.__GameUI.hideturtle()
        self.__GameUI.penup()
        self.__GameUI.color("white")
        self.new_asteroid()
        self.new_enemy_spaceship()
        self.__GameUI.getscreen().onkey(self.player_shoot, "space")
        self.__GameUI.getscreen().listen()
        self.__T.getscreen().update()
        self.update_objects()

    def field(self):
        self.__T.goto(self.__game_data["field_info"][0][0], self.__game_data["field_info"][0][1])
        self.__T.pendown()
        for line in range(0, 4, 1):
            if line % 2==0:
                self.__T.fd(self.__game_data["field_info"][4]["Size1"])
                self.__T.rt(90)
            else:
                self.__T.fd(self.__game_data["field_info"][4]["Size2"])
                self.__T.rt(90)   
        self.__T.penup()
        self.__T.getscreen().update()       

    def new_asteroid(self):
        asteroid = Asteroid(randint(self.__game_data["field_info"][0][0]+35,self.__game_data["field_info"][1][0]-35), randint(self.__game_data["field_info"][0][1]+35, self.__game_data["field_info"][0][1]+55), self.__game_data["field_info"], randint(-5, -2), "gray", 1, randint(1, 3), True)
        self.__game_data["objects"].append(asteroid)

    def new_enemy_spaceship(self):
        enemy_space_ship = EnemyShip(randint(self.__game_data["field_info"][0][0]+35,self.__game_data["field_info"][1][0]-35), randint(self.__game_data["field_info"][0][1]+35, self.__game_data["field_info"][0][1]+55), self.__game_data["field_info"], 0, randint(-6, -3), "slategray", "triangle", 1, randint(2, 3), True)
        self.__game_data["objects"].append(enemy_space_ship)

    def new_bonus(self):
        bonus_types = ("Shield_bonus", "Score_bonus")
        bonus_type = choice(bonus_types)
        if bonus_type == "Shield_bonus":
            bonus = ShieldBonus(randint(self.__game_data["field_info"][0][0]+35,self.__game_data["field_info"][1][0]-35), randint(self.__game_data["field_info"][0][1]+35, self.__game_data["field_info"][0][1]+55), self.__game_data["field_info"], randint(-10, -5), "cyan", 1, True)
            self.__game_data["objects"].append(bonus)
        elif bonus_type == "Score_bonus":
            bonus = ScoreBonus(randint(self.__game_data["field_info"][0][0]+35,self.__game_data["field_info"][1][0]-35), randint(self.__game_data["field_info"][0][1]+35, self.__game_data["field_info"][0][1]+55), self.__game_data["field_info"], randint(-10, -5), "yellow", 1, randint(25, 50), True)
            self.__game_data["objects"].append(bonus)            

    def enemy_collide(self, enemy):
        if not isinstance(enemy, Projectile):
            if self.__game_data["player"].distance(enemy) <= 20:
                if self.__game_data["player"].shield.health > 0:
                    self.__game_data["player"].shield.take_damage(enemy.damage)
                    print(" ")
                    print(f"\nЩит пошкоджено! Залишилось: {self.__game_data['player'].shield.health}\n")
                    enemy.destroy()
                    return True, True
                else:
                    print(" ")
                    print(f"\nСтанцію знищено... Очки: {self.__game_data['score']}")
                    self.__GameUI.goto(-50, -5)
                    self.__GameUI.pendown()
                    self.__GameUI.write("Станцію знищено!", font=("Arial", 15))
                    self.__game_data["game_going"] = False
                    self.__game_data["player"].destroy()
                    enemy.destroy()
                    return False, True
            else:
                return True, False
        else:
            collision_detected = False
            for obj in self.__game_data["objects"]:
                if not isinstance(obj, SpaceShip) and not isinstance(obj, Projectile):
                    if obj.active:
                        if obj.distance(enemy) <= 20:
                            collision_detected = True
                            if not isinstance(obj, Bonus):
                                obj.health_to_delete -= enemy.damage
                                if obj.health_to_delete <= 0:
                                    if isinstance(obj, EnemyShip):
                                        self.__game_data["score"] += 50
                                    elif isinstance(obj, Asteroid):
                                        self.__game_data["score"] += 25
                                    obj.destroy()
                                enemy.destroy()
                                break
                            else:
                                obj.apply_effect(self.__game_data)
                                obj.destroy()
                                enemy.destroy()
                                break
            if collision_detected:
                return True, True
            else:
                return True, False

    def bonus_collide(self, bonus):
        if self.__game_data["player"].distance(bonus) <= 20:
            bonus.apply_effect(self.__game_data)
            bonus.destroy()
            return True, True
        else:
            return True, False     

    def get_UI_data(self):
        texts_to_write = {
            "Score": self.__game_data["score"],
            "Shield": self.__game_data["player"].shield.health,
            "Weapon": self.__game_data["player"].weapon_equiped
        }
        return texts_to_write

    def update_UI(self):
        self.__GameUI.clear()
        texts_to_write = self.get_UI_data()
        for UI_Key in self.__game_data["UI_texts"]:
            UI_Text = self.__game_data["UI_texts"][UI_Key]
            coordinates = UI_Text[1]
            self.__GameUI.goto(coordinates[0], coordinates[1])
            self.__GameUI.pendown()
            self.__GameUI.write(f"{UI_Text[0]}{texts_to_write[UI_Key]}", font=("Arial", 15))
            self.__GameUI.penup()

    def player_shoot(self):
        if self.__game_data["game_going"]:
            projectile = self.__game_data["player"].shoot()
            if projectile is not None:
                self.__game_data["objects"].append(projectile)

    def update_objects(self):
        if self.__game_data["game_going"]:
            self.update_UI()
            if self.__game_data["score"] >= 200:
                print(" ")
                print(f"\nТи врятував станцію! Очки: {self.__game_data['score']}\n")
                self.__GameUI.goto(-50, -5)
                self.__GameUI.pendown()
                self.__GameUI.write("Ти врятував станцію!", font=("Arial", 15))
                self.__game_data["player"].destroy()
                self.__game_data["game_going"] = False
        if self.__game_data["game_going"]:
            print(f"\rЩит: {self.__game_data['player'].shield.health} | Очки: {self.__game_data['score']} | Зброя: {self.__game_data['player'].weapon_equiped}", end="", flush=True)
            if self.__game_data["asteroid_spawn_timer"] >= self.__game_data["asteroid_spawn_interval"]:
                self.new_asteroid()
                self.__T.getscreen().update()
                self.__game_data["asteroid_spawn_timer"] = 0
            if self.__game_data["enemy_spaceship_spawn_timer"] >= self.__game_data["enemy_spaceship_spawn_interval"]:
                self.new_enemy_spaceship()
                self.__T.getscreen().update()
                self.__game_data["enemy_spaceship_spawn_timer"] = 0
            if self.__game_data["bonus_spawn_timer"] >= self.__game_data["bonus_spawn_interval"]:
                self.new_bonus()
                self.__T.getscreen().update()
                self.__game_data["bonus_spawn_timer"] = 0
            objects_to_delete = []
            for object in self.__game_data["objects"]:
                collision = False
                continue_game = True
                if not object.active:
                    objects_to_delete.append(object)
                else:
                    if isinstance(object, SpaceShip):
                        continue_game, collision = True, False
                    elif isinstance(object, (Asteroid, EnemyShip)):
                        continue_game, collision = self.enemy_collide(object)                       
                    elif isinstance(object, Bonus):
                        continue_game, collision = self.bonus_collide(object)
                    elif isinstance(object, Projectile):
                        continue_game, collision = self.enemy_collide(object) 
                    else:
                        print(" ")
                        print("\nНевідомий об'єкт!\n")
                    if collision:
                        objects_to_delete.append(object)
                        if not continue_game:
                            objects_to_delete.append(self.__game_data["player"])
                            break
                    else:
                        score_change = object.update()
                        if score_change is not None:
                            new_score = max(0, self.__game_data["score"] + score_change)
                            if self.__game_data['score']-new_score > 0:
                                print(" ")
                                print(f"\nУ станцію врізався ворожий корабель... -{self.__game_data['score']-new_score} очок!\n")
                            self.__game_data["score"] = new_score
            for object in objects_to_delete:
                self.__game_data["objects"].remove(object)
            objects_to_delete.clear()
            if not self.__game_data["game_going"]:
                for object in self.__game_data["objects"]:
                    object.hideturtle()
            self.__T.getscreen().update()
            self.__game_data["asteroid_spawn_timer"] += 50
            self.__game_data["enemy_spaceship_spawn_timer"] += 50
            self.__game_data["bonus_spawn_timer"] += 50
            for launcher_key in self.__game_data["player"].weapons:
                launcher = self.__game_data["player"].weapons[launcher_key]
                launcher.reloading_timer += 50
            self.__T.getscreen().ontimer(self.update_objects, 50)
        else:
            if not self.__game_data["game_going"]:
                for object in self.__game_data["objects"]:
                    object.hideturtle()
            self.__T.getscreen().update()

field_coordinates = (
    (-200, 150), 
    (200, 150),
    (200, -150),
    (-200, -150),
    {"Size1": 400, "Size2": 300}
                     )
for_game_UI = {
    "Score": ("Очки: ", (100, 175)),
    "Shield": ("Здоров'я щита: ", (-185, -175)),
    "Weapon": ("Зброя: ", (-200, 175))
}

game = Game(field_coordinates, for_game_UI)
screen.update()
done()
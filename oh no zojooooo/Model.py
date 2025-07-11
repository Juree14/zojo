import json
from mailbox import _singlefileMailbox
from tkinter import Y
import turtle

class Game():
    def __init__(self):
        #admin mode
        self.admin_mode = False
        
        self.running = True
        self.atk = None
        self.defense = None
        self.spd = None
        self.dge = None
        self.denar = 10

        self.movement_speed = 150
        self.delta_time = 0
        
        self.game_n = None
        self.mode = "zacetek"
        self.curent_mode = None
        self.x = 0
        self.y = 0
        self.hp = 100
        self.golem_alive = True
        self.igralec = None
        self.collisions = {
                "svet": [
                    (65, 300, 400, 50, 0),
                    (-400, -80, -364, -237, 1),
                    (-392, -219, 391, -291, 2),
                    (362, -80, 400, -300, 3),
                    (-396, 297, -311, 20, 4),
                    (-330, 295, -100, 201, 5)
                ],
                "zacetna_hisa": [
                    (1000, 1000, 1000, 1000, 0)
                ],
                "svet_desno": [
                    (-395, 293, -378, 50, 0),
                    (-394, 294, -136, 103, 1),
                    (-180, 290, 60, 169, 2),
                    (55, 176, 389, 93, 3),
                    (-397, -83, -385, -286, 4),
                    (-383, -209, -199, -290, 5),
                    (-227, -133, -147, -289, 6),
                    (-163, -55, 23, -169, 7),
                    (9, -131, 389, -287, 8),
                    (379, -50, 400, -300, 9)
                ],
                "svet_levo": [
                    (-250, 50, 30, -195, 0),
                    (-400, -250, 400, -300, 1),
                    (-400, 300, -380, -300, 2),
                    (-400, 300, 400, 280, 3),
                    (380, 300, 400, 20, 4),
                    (380, -100, 400, -300, 5)
                ],
                "start_fight": [
                    (-400, 300, 400, -300, 0)
                ],
                "fight_screen_monster": [
                    (-400, 300, 400, -300, 0)
                ],
                "weapons": [
                    (-400, 300, 400, -300, 0)
                ],
                "trgovina": [(1000, 1000, 1000, 1000, 0)
                ]
            }
        self.objects = {
        "svet" : [(230, 50, 310, 44, "zacetna_hisa"), (390, 100, 400, -100,"svet_desno"),(-400, 100, -390, -100,"svet_levo")],
        "zacetna_hisa" : [(-50, -245, 50, -1000,"svet"),(-60, 300, 60, 90, "chest")],
        "svet_desno" : [(-400, 100, -390, -100,"svet")],
        "svet_levo" : [(390, 100, 400, -100,"svet"), (-130, -195, -90, -205, "trgovina")],
        'start_fight' : [(1000,1000,1000,1000,"neki")],
        'fight_screen_monster' : [(1000,1000,1000,1000,"neki")],
        "trgovina":[(-50, -245, 50, -1000, "svet_levo")]
        }
        self.monsters = [Monster(50, 5, 5, 5, 5, 250, 0, "svet_desno", 'oh no zojooooo\\slike\\golem.gif', "true")]
        self.player_attacked = False
        self.monster_attacked = False
        self.inventory_on = False
        self.menu_True = False
        self.number_of_hearts = 3
        self.ui_srcka = []
        self.have_wooden_sword = True
        self.wooden_sword_value = False
        self.atk_value = 1
        self.def_value = 1
        self.spd_value = 1
        self.dge_value = 1
        self.new_load1 = "NEW GAME"
        self.new_load2 = "NEW GAME"
        self.new_load3 = "NEW GAME"
        self.menu = None
        self.current_monster = None
        self.menu_open = False
        self.curent_mode = None

        self.ui_hp = None
        self.inventory_items = {}
        self.inventory_buttons = {}
        self.ozadja = {
            "svet": Ozadje("oh no zojooooo\\slike\\svet1.gif"),
            "zacetna_hisa": Ozadje("oh no zojooooo\\slike\\zacetna_hisa.gif"),
            "svet_desno": Ozadje("oh no zojooooo\\slike\\svet2.gif"),
            "svet_levo": Ozadje("oh no zojooooo\\slike\\svet_levo.gif"),
            "fight_screen_monster": Ozadje("oh no zojooooo\\slike\\prozorno_ozadje.gif"),
            "trgovina": Ozadje("oh no zojooooo\\slike\\prozorno_ozadje.gif")
        }
        self.stat_roll = {
            "atk_pressed": False,
            "def_pressed": False,
            "spd_pressed": False,
            "dge_pressed": False,
            "atk_value": None,
            "def_value": None,
            "spd_value": None,
            "dge_value": None,
            "atk_turtle": None,
            "def_turtle": None,
            "spd_turtle": None,
            "dge_turtle": None,
            "min": 1,
            "atk_adjusted": False,
            "def_adjusted": False,
            "spd_adjusted": False,
            "turtles": [],     
            "kvadrati": []     
        }
        self.sobe = {
            "svet": Soba("svet", self.ozadja["svet"], self.collisions["svet"], self.objects["svet"], self.monsters),
            "zacetna_hisa": Soba("zacetna_hisa", self.ozadja["zacetna_hisa"], self.collisions["zacetna_hisa"], self.objects["zacetna_hisa"]),
            "svet_desno": Soba("svet_desno", self.ozadja["svet_desno"], self.collisions["svet_desno"], self.objects["svet_desno"]),
            "svet_levo": Soba("svet_levo", self.ozadja["svet_levo"], self.collisions["svet_levo"], self.objects["svet_levo"]),
            "fight_screen_monster": Soba("fight_screen_monster", self.ozadja["fight_screen_monster"], self.collisions["fight_screen_monster"]),
            "trgovina": Soba("trgovina", self.ozadja["trgovina"], self.collisions["trgovina"], self.objects["trgovina"])
        }



    def set_atk(self, atk):
        self.atk = atk

    def set_def(self, defense):
        self.defense = defense

    def set_spd(self, spd):
        self.spd = spd

    def set_dge(self, dge):
        self.dge = dge

    def set_hp(self, hp):
        self.hp = hp

    def set_mode(self, mode):
        self.mode = mode

    def set_game_n(self, game_n):
        self.game_n = game_n

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_golem_alive(self,alive):
        self.golem_alive = alive


    def to_json(self):
        return{
            "atk" : self.atk,
            "def" : self.defense,
            "spd" : self.spd,
            "dge" : self.dge,
            "denar": self.denar,
            "game_n": self.game_n,
            "mode" : self.mode,
            "x" : self.x,
            "y" : self.y,
            "hp": self.hp,
            "objects": self.objects,
            "monsters": [monster.to_json() for monster in self.monsters]
            }

    def save_game(self, fname):
        with open(fname, "w", encoding= "UTF-8") as dat:
            json.dump(self.to_json(), dat)

    def load_game(self, fname):
        with open(fname, encoding= "UTF-8") as dat:
            self.from_json(json.load(dat))
    
    def from_json(self,state):
        self.atk = state["atk"]
        self.defense = state["def"]
        self.spd = state["spd"]
        self.dge = state["dge"]
        self.denar = state["denar"]
        self.game_n = state["game_n"]
        self.mode = state["mode"]
        self.x = state["x"]
        self.y = state["y"]
        self.hp = state["hp"]

        self.monsters = [Monster.from_json(monster) for monster in state["monsters"]]
        # Po nalaganju razporedi pošasti v ustrezne sobe
        for soba in self.sobe.values():
            soba.monsters = []
        for monster in self.monsters:
            if monster.svet in self.sobe:
                self.sobe[monster.svet].monsters.append(monster)

    def is_menu_open(self):
        return self.menu_open

    def toggle_inventory(self):
        self.inventory_on = not self.inventory_on




class Master():
    def __init__(self):
        self.game1 = None
        self.game2 = None
        self.game3 = None

    def set_game_1(self, game1):
        self.game1 = game1
    
    def set_game_2(self, game2):
        self.game2 = game2

    def set_game_3(self, game3):
        self.game3 = game3

    def to_json(self):
        return{
            "game1" : self.game1,
            "game2" : self.game2,
            "game3" : self.game3
            }

    def save_game(self, name):
        with open(name, "w", encoding= "UTF-8") as dat:
            json.dump(self.to_json(), dat)

    def load_game(self, name):
        with open(name, encoding= "UTF-8") as dat:
            self.from_json(json.load(dat))
    
    def from_json(self,state):
        self.game1 = state["game1"]
        self.game2 = state["game2"]
        self.game3 = state["game3"]


class Monster():
    def __init__(self, hp, atk, defense, spd, dge, x, y, svet, slika, alive):
        self.monster_hp = hp
        self.monster_atk = atk
        self.monster_def = defense
        self.monster_spd = spd
        self.monster_dge = dge
        self.monster_x = x
        self.monster_y = y
        self.alive = alive
        self.img = slika
        self.svet = svet

        self.monster = turtle.Turtle()
        self.monster.speed(0)
        self.monster.shape(self.img)
        self.monster.penup()
        self.monster.goto(self.monster_x,self.monster_y)
        self.monster.hideturtle()

    def set_alive(self, alive):
        self.alive = alive

    def fight_monster(self, x, y, mode):
        if self.alive and (self.svet == mode):
            return self.monster_x - 70 < x < self.monster_x + 70 and self.monster_y - 50 < y < self.monster_y + 90
        else:
            pass


    def to_json(self):
        return{
            "atk" : self.monster_atk,
            "def" : self.monster_def,
            "spd" : self.monster_spd,
            "dge" : self.monster_dge,
            "slika": self.img,
            "svet" : self.svet,
            "x" : self.monster_x,
            "y" : self.monster_y,
            "hp": self.monster_hp,
            "alive" : self.alive,
            }
    @classmethod
    def from_json(cls,state):
        return cls(state["hp"],state["atk"],state["def"],state["spd"],state["dge"],state["x"],state["y"],state["svet"],state["slika"],state["alive"])

        

class Button:
    def __init__(self, x, y, width, height, text, font=("gameovercre", 30, "normal"), color="white", text_offset=(35, 25)):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.text = text
        self.font = font
        self.text_offset = text_offset
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.speed(0)
        self.color = color

    def draw(self):
        self.turtle.fillcolor(self.color)
        self.turtle.begin_fill()
        self.turtle.goto(self.x, self.y)
        self.turtle.goto(self.x + self.width, self.y)
        self.turtle.goto(self.x + self.width, self.y + self.height)
        self.turtle.goto(self.x, self.y + self.height)
        self.turtle.goto(self.x, self.y)
        self.turtle.end_fill()
        self.turtle.goto(self.x + self.text_offset[0], self.y + self.text_offset[1])
        self.turtle.write(self.text, font=self.font)

    def is_clicked(self, click_x, click_y):
        return self.x <= click_x <= self.x + self.width and self.y <= click_y <= self.y + self.height

    def clear(self):
        self.turtle.clear()


class InventoryItem:
    def __init__(self, image, slot_index=None, category=None, position_hidden=(1000, 1000)):
        self.slot_index = slot_index  # številka slota (0–11)
        self.category = category      # "weapons" ali "items"
        self.turtle = turtle.Turtle()
        self.turtle.shape(image)
        self.turtle.penup()
        self.turtle.speed(0)
        self.hide(position_hidden)

    def move_to(self, x, y):
        self.turtle.goto(x, y)

    def hide(self, position=(1000, 1000)):
        self.move_to(*position)


class UIStat:
    def __init__(self, x, y, value, color="#FEDA41"):
        self.value = value
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.color(color)
        self.turtle.goto(x, y)
        self.update(value)

    def update(self, new_value):
        self.turtle.clear()
        self.turtle.write(str(new_value), font=("gameovercre", 16, "normal"))

    def clear(self):
        self.turtle.clear()

class Ozadje:
    def __init__(self, image, position_hidden=(1000, 1000)):
        self.turtle = turtle.Turtle()
        self.turtle.shape(image)
        self.turtle.penup()
        self.turtle.speed(0)
        self.hide(position_hidden)

    def show(self, x=0, y=0):
        self.turtle.goto(x, y)

    def hide(self, position=(1000, 1000)):
        self.turtle.goto(*position)

    def set_position(self, x, y):
        self.turtle.goto(x, y)


class Soba:
    def __init__(self, ime, ozadje, collisions=None, objects=None, monsters=None):
        self.ime = ime
        self.ozadje = ozadje
        self.collisions = collisions if collisions is not None else []
        self.objects = objects if objects is not None else []
        self.monsters = monsters if monsters is not None else []

    def to_json(self):
        return {
            "ime": self.ime,
            "ozadje": self.ozadje,  # Lahko shraniš ime slike ali pot
            "collisions": self.collisions,
            "objects": self.objects,
            "monsters": [monster.to_json() for monster in self.monsters]
        }

    @classmethod
    def from_json(cls, data):
        monsters = [Monster.from_json(m) for m in data.get("monsters", [])]
        return cls(
            ime=data["ime"],
            ozadje=data["ozadje"],
            collisions=data.get("collisions", []),
            objects=data.get("objects", []),
            monsters=monsters
        )

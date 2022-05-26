import json
from mailbox import _singlefileMailbox
from tkinter import Y
import turtle

class Game():
    def __init__(self):
        self.atk = None
        self.defense = None
        self.spd = None
        self.dge = None
        self.game_n = None
        self.mode = None
        self.x = 0
        self.y = 0
        self.hp = 0
        self.golem_alive = True
        self.objects = {
        "svet" : [(230, 50, 310, 44, "zacetna_hisa"), (390, 100, 400, -100,"svet_desno"),(-400, 100, -390, -100,"svet_levo")],
        "zacetna_hisa" : [(-50, -245, 50, -1000,"svet"),(-60, 300, 60, 90, "chest")],
        "svet_desno" : [(-400, 100, -390, -100,"svet")],
        "svet_levo" : [(390, 100, 400, -100,"svet")],
        'start_fight' : [(1000,1000,1000,1000,"neki")],
        'fight_screen_monster' : [(1000,1000,1000,1000,"neki")]
        }
        self.monsters = [Monster(50, 5, 5, 5, 5, 250, 0, "svet_desno", 'slike\golem.gif', "true")]
        


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
        self.game_n = state["game_n"]
        self.mode = state["mode"]
        self.x = state["x"]
        self.y = state["y"]
        self.hp = state["hp"]

        self.monsters = [Monster.from_json(monster) for monster in state["monsters"]]
        




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

        



import json
from mailbox import _singlefileMailbox
from tkinter import Y

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

    def set_atk(self, atk):
        self.atk = atk

    def set_def(self, defense):
        self.defense = defense

    def set_spd(self, spd):
        self.spd = spd

    def set_dge(self, dge):
        self.dge = dge

    def set_mode(self, mode):
        self.mode = mode

    def set_game_n(self, game_n):
        self.game_n = game_n

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
    
    def to_json(self):
        return{
            "atk" : self.atk,
            "def" : self.defense,
            "spd" : self.spd,
            "dge" : self.dge,
            "game_n": self.game_n,
            "mode" : self.mode,
            "x" : self.x,
            "y" : self.y
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


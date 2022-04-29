import json

class Game():
    def __init__(self):
        self.atk = None
        self.game_n = None

    def set_atk(self, atk):
        self.atk = atk

    def set_game_n(self, game_n):
        self.game_n = game_n


    def to_json(self):
        return{
            "atk" : self.atk,
            "game_n": self.game_n
            }

    def save_game(self, fname):
        with open(fname, "w", encoding= "UTF-8") as dat:
            json.dump(self.to_json(), dat)

    def load_game(self, fname):
        with open(fname, encoding= "UTF-8") as dat:
            self.from_json(json.load(dat))
    
    def from_json(self,state):
        self.atk = state["atk"]
        self.game_n = state["game_n"]



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


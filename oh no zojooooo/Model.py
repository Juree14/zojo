import json

class Game():
    def __init__(self):
        self.atk = None
    

    def set_atk(self, atk):
        self.atk = atk

    def to_json(self):
        return{
            "atk" : self.atk
            }

    def save_game(self, fname):
        with open(fname, "w", encoding= "UTF-8") as dat:
            json.dump(self.to_json(), dat)

    def load_game(self, fname):
        with open(fname, encoding= "UTF-8") as dat:
            self.from_json(json.load(dat))
    
    def from_json(self,state):
        self.atk = state["atk"]



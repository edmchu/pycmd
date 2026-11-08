from ast import Pass
import json
import connector

class loader:
    def __init__(self):
        self.Plib = json.load(open("data/Plib.json"))
        self.Slibs = {}
    
    def loadSlib(self, SlibName):
        self.Slibs[SlibName] = json.load(open(f"data/{SlibName}.json"))
        return Pass
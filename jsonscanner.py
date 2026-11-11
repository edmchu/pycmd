
import json

class jsonscanner:
    def getfilecomponent(self, file, *positions):
        with open(file, "r") as f:
            filecontents = json.load(f)
        for pos in positions:
            filecontents = filecontents[pos]
            return filecontents

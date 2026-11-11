
import json

class jsoninterface:
    def getfilecomponent(self, file, address):
        with open(file, "r") as f:
            filecontents = json.load(f)
        for pos in address.split("@"):
            filecontents = filecontents[pos]
        return filecontents

    def addcomponnent(self, file, value, *position):
        with open(file, "r") as f:
            filecontents = json.load(f)
        target = filecontents
        for pos in position[:-1]:
            target = target[pos]
        target[position[-1]] = value

        with open(file, "w") as f:
            json.dump(filecontents, f, indent=4)

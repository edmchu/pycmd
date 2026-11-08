
class parser:
    def __init__(self):
        self.cmd = None

    def getcmdname(self, cmd):
        return cmd.split(" ;")[0]

    def getcmdargs(self, cmd, arg):
        return cmd.split(" ;")[arg]
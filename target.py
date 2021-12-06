import build
import script

class Target:
    def __init__(self, name, modes, builds, postexecs):
        self.name = name
        self.modes = modes
        self.builds = builds
        self.postexes = postexecs

    def run(mode = ''):
        pass

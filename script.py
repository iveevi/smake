import os

class Script:
    def __init__(self, *kargs):
        self.scripts = kargs

    def run(self, *args):
        for script in self.scripts:
            ret = os.system(script.format(*args))

            # TODO: print error
            if (ret != 0):
                exit(-1)

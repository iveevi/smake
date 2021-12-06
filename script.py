import os

class Script:
    def __init__(self, *kargs):
        self.scripts = kargs

    def run(self):
        for script in self.scripts:
            ret = os.system(script)

            if (ret != 0):
                exit(-1)

import build
import script

class Target:
    def __init__(self, name, modes, builds, postexecs):
        self.name = name
        self.modes = modes
        self.builds = builds
        self.postexecs = postexecs

    def run(self, mode = 'default'):
        # Empty is always a valid mode, but `default should be used'
        if len(mode) == 0:
            mode = 'default'
        
        # Retrieve run attributes
        build = self.builds[mode]
        postexec = self.postexecs[mode]

        # Run the build
        target = build.run()

        # TODO: Run postexec with target argument
        postexec.run(target)
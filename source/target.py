import source.build
import source.script

from source.colors import colors

class Target:
    def __init__(self, name, modes, builds, postbuilds):
        self.name = name
        self.modes = modes
        self.builds = builds
        self.postbuilds = postbuilds

    def run(self, mode = 'default'):
        # Empty is always a valid mode, but `default should be used'
        if len(mode) == 0:
            mode = 'default'
        
        # Retrieve run attributes
        build = self.builds[mode]

        # Run the build
        target = build.run()

        # Run postbuild with target argument, if present
        if mode in self.postbuilds:
            if len(target) == 0:
                print(colors.FAIL + '\nFailed to compile target, skipping postbuild script' + colors.ENDC)
                return

            postbuild = self.postbuilds[mode]
            print(colors.OKBLUE + '\nSucessfully compiled target, ' + \
                'running postbuild script\n' + colors.ENDC)
            postbuild.run(target)
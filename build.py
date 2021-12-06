import os

from colors import colors

class Build:
    cache = '.smake'
    bdir = '.smake/builds'
    tdir = '.smake/targets'

    # TODO: each build should have a name
    # Build is build name
    def __init__(self, target, build, sources, idirs = [], libs = [], flags = []):
        # Set immediate properties
        self.target = target
        self.build = build
        self.sources = sources
        self.compiler = 'g++'

        # TODO: make function for directory creation
        # Create the cache directory
        if not os.path.exists(self.cache):
            os.mkdir(self.cache)

        # Create build dir
        if not os.path.exists(self.bdir):
            os.mkdir(self.bdir)
        
        # Create the output directory
        self.odir = self.bdir + '/' + self.build
        if not os.path.exists(self.odir):
            os.mkdir(self.odir)
        
        # Create target build directory
        self.tpath = self.tdir + '/' + self.target
        if not os.path.exists(self.tdir):
            os.mkdir(self.tdir)

        # Includes
        # TODO: filter includes, check if they exist
        self.idirs = ''
        if len(idirs) > 0:
            self.idirs = ''.join([' -I ' + idir for idir in idirs])

        # Libraries
        self.libs = ''
        if len(libs) > 0:
            self.libs = ''.join([' -l' + lib for lib in libs])

        # Flags
        self.flags = ''
        if len(flags) > 0:
            self.flags = ''.join(flags)

    def compile(self, file):
        # Check if file exists
        if not os.path.exists(file):
            print(colors.FAIL + f'\tFile {file} does not exist' + colors.ENDC)
            return ''

        # Get file name without directory
        fname = os.path.basename(file)

        # Create the output file
        ofile = os.path.join(self.odir, fname.replace('.cpp',
            '.o').replace('.c', '.o'))

        # Check if compilation is necessary
        file_t = os.path.getmtime(file)
        if os.path.exists(ofile):
            ofile_t = os.path.getmtime(ofile)
            if ofile_t > file_t:
                return ofile

        # Compile the source
        cmd = '{} {} -c -o {} {} {}'.format(self.compiler, self.flags,
                ofile, file, self.idirs)
        ret = os.system(cmd)
        
        # Check if compilation failed
        if ret != 0:
            return ''

        # Return object
        return ofile

    # TODO: add option for verbose
    def run(self):
        # List of compiled files
        compiled = []

        # Compilation failure flag
        failed = False

        # Failed sources
        fsources = []

        # Generate format string
        slen = str(len(self.sources))
        fstr = colors.OKCYAN + '[{:>' + str(len(slen)) + '}/' + slen + '] ' \
            + colors.OKGREEN + 'Compiling {}' + colors.ENDC

        # Compile the sources
        for i in range(len(self.sources)):
            # Print the message
            print(fstr.format(i + 1, self.sources[i]))

            # Compile the file (or attempt to)
            ofile = self.compile(self.sources[i])

            # Check failure
            if len(ofile) == 0:
                fsources.append(self.sources[i])
                failed = True

            # Add to compiled list
            compiled.append(ofile)

        # Check if any of the sources failed to compile
        if failed:
            # Print message
            print('\n' + colors.FAIL + 'Failed to compile the' + \
                ' following sources,' + ' skipping linking process' + \
                colors.ENDC)

            # Print failed sources
            for file in fsources:
                print(colors.PURPLE + '\t' + file + colors.ENDC)

            # Return empty for failure
            return ''
        else:
            # Command generation
            compiled_str = ' '.join(compiled)
            cmd = f'{self.compiler} {compiled_str} -o {self.tpath} {self.libs}'

            # Print message
            print(colors.OKBLUE + f'Linking executable {self.target}' + colors.ENDC)

            # Check return of linking
            ret = os.system(cmd)
            if ret != 0:
                # Print message and return empty
                print(colors.FAIL + f'Failed to link target {self.target}' + \
                        colors.ENDC)

                return ''

        # Return the location of the target
        return self.tpath

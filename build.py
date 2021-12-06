import os

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Build:
    cache = '.smake'
    odir = '.smake/build'
    tdir = '.smake/target'

    def __init__(self, target, sources, idirs = [], libs = [], flags = ''):
        self.target = target
        self.sources = sources
        self.flags = flags

        self.compiler = 'g++'

        # Create the cache directory
        if not os.path.exists(self.cache):
            os.mkdir(self.cache)
        
        # Create the output directory
        if not os.path.exists(self.odir):
            os.mkdir(self.odir)
        
        # Create target build directory
        self.tpath = self.tdir + '/' + self.target
        if not os.path.exists(self.tdir):
            os.mkdir(self.tdir)

        # Includes
        # TODO: filter includes
        if len(idirs) > 0:
            self.idirs = ''.join([' -I ' + idir for idir in idirs])
        else:
            self.idirs = ''

        # Libraries
        self.libs = ''
        if len(libs) > 0:
            self.libs = ''.join([' -l' + lib for lib in libs])

    def compile(self, file):
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
        os.system(cmd)
        
        # TODO: check error

        return ofile

    # TODO: add option for verbose
    def run(self):
        # List of compiled files
        compiled = []

        # Generate format string
        slen = str(len(self.sources))
        fstr = colors.OKCYAN + '[{:>' + str(len(slen)) + '}/' + slen + '] ' \
            + colors.OKGREEN + 'Compiling {}' + colors.ENDC

        # Compile the sources
        for i in range(len(self.sources)):
            # TODO: show the target building message

            # Print
            # print(f'[{i + 1}/{len(self.sources)}] Compiling {self.sources[i]}')
            print(fstr.format(i + 1, self.sources[i]))
            ofile = self.compile(self.sources[i])

            # TODO: check failure

            # Add to compiled list
            compiled.append(ofile)
        
        # Compile all the objects
        # TODO: skip if any source failed to compile
        #   keep compiling other ones though
        cmd = '{} {} -o {} {}'.format(self.compiler, ' '.join(compiled),
            self.tpath, self.libs)
        print(colors.OKBLUE + f'Linking executable {self.target}' + colors.ENDC)
        # print(cmd)

        os.system(cmd)

        # Return the location of the target
        return self.tpath

# smake

Smake is a simple and convenient build-and-run system for C and C++ projects.

## Why make another build system?

CMake and GNU Make are great build systems. However, as the project gets larger, and as there are increasingly many types of builds (e.g. a builds for debugging), it becomes tedious to add duplicate code.

Smake solves this problem with its target-mode-build hierarchy. In this system,
every project has a set of targets, and each target has a set of build modes. When
smake is run on a target with a specific build mode, it will run the build 
corresponding to that mode.

![pictures/smake.png](https://github.com/vedavamadathil/smake/blob/main/pictures/smake.png?raw=true)

Each mode also has a post-build script that can be run. For most builds, this will
simply be executing the target object file, but in some cases, the user may want
to run a different command (i.e. `gdb` or `valgrind`) with the object file.

## Install

Smake can be installed easily with `pip install smake`.

One can also simply clone the source and link the `smake` executable.

## How does it work?

Smake searches for a `smake.yaml` file in the current directory and creates configurations for each target, including all modes and their 
corresponding builds and post-build scripts, etc.

The structure of an `smake` configuration file is as follows (in no strict 
order):

```yaml
# Variables that can be referenced in builds
definitions:
  - gsourceA: fileA.c, fileB.c

# List of builds that will be used by the targets
builds:
  - buildA:
    - sources: gsourceA     # Reference a group of sources defined
                            # in the sources section
  - buildB:
    - sources: main.c       # Sources can be specified in the build as well
    - flags: -Wall, -Wextra # Flags are specified here, can be comma
                            # separated or specified as a list  
  - buildC:
    - sources: main.c
    - flags:  -Wall, -Wextra, -g

# List of all targets
targets:
 - targetA:
  - modes: default          # Specifiy modes here (default mode does
                            # not really need to be specified)
  - builds:
    - default: buildA       # Must specify builds as a pair of `mode: build`
  
  # Note that post-build scripts do not need to be specified:
  #   if nothing is specified, then there is no post-build script
  - targetB:
    - modes: default, debug # Comma separated modes
    - builds:               # Modes are selected using the -m option of smake
      - default: buildB     #   for example: smake targetB -m debug
      - debug: buildC       # the default mode is used if no mode is specified
    - postbuild:            # Post-build scripts, specified per mode (optional)
      - debug: 'gdb {}'     # The {} is replaced by the target object file
```

This configuration allows for the following commands:

```bash
$ smake targetA
$ smake targetB
$ smake targetB -m debug
```

As one can imagine, this build system is quite simple, yet powerful.

Another example of `smake` file can be found inside the `example` directory.
Clone this repository and run `smake` to get started (available targets are
`smake basic` and `smake multisource`).

## Future features

- [ ] Pre-build scripts, for cases where source code needs to be auto-generated
- [ ] Add options for parallelizing builds
- [ ] Easier way to define macro arguments for the compilers
- [ ] Detect changes in included headers, and the config in general
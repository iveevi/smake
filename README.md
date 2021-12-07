# smake

Smake is a simple and convenient build-and-run system for C and C++ projects.

# Why make another build system?

CMake and GNU Make are great build systems. However, as the project gets larger, and as there are increasingly many types of builds (e.g. a builds for debugging), it becomes tedious to add duplicate code.

Smake solves this problem with its target-mode-build hierarchy.

# Install

Smake can be installed easily with `pip install smake`.

One can also simply clone the source and link the `smake` executable.

# How does it work?

Smake searches for all `smake.yaml` files in the current directory, recursively, and creates the configurations for each target, including all modes and their corresponding builds and post-build scripts, etc.

import setuptools

# Create the package
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
        name = 'smake',
        version = '1.2.5',
        scripts = ['smake'],
        author = "Venkataram Edavamadathil Sivaram",
        author_email = "vesion4690@gmail.com",
        description = "A simple and convenient build-and-run system for C and C++.",
        long_description = long_description,
        long_description_content_type = "text/markdown",
        url = "https://github.com/vedavamadathil/smake",
        packages = setuptools.find_packages(),
        instal_requires = ['pyyaml', 'colorama'],
        classifiers = [
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
        ],
)

import yaml
import build

def preprocess(d, pr):
    prop = d[pr]
    if isinstance(prop, str):
        prop = prop.split(', ')
    return prop

def load_smake(file):
    with open(file, 'r') as file:
        smake = yaml.safe_load(file)

    print(smake)

    name = list(smake)[0]
    properties = {}
    for d in smake[name]:
        properties.update(d)
    print(properties)

    # Preprocess properties
    sources = preprocess(properties, 'sources')
    includes = preprocess(properties, 'includes')
    libraries = preprocess(properties, 'libraries')
    flags = preprocess(properties, 'flags')

    return build.Build('example', name, sources, includes, libraries, flags)

build = load_smake('example.yaml')
build.run()

import yaml

from build import Build
from target import Target
from script import Script

# Predefined groups of sources
predefined = dict()

# TODO: put into a config class
def process(d, pr):
    prop = d[pr]
    if isinstance(prop, str):
        prop = prop.split(', ')
    
    for i in range(len(prop)):
        if prop[i] in predefined:
            prop[i] = predefined[prop[i]]

    return prop

def concat(ldicts):
    out = {}
    for d in ldicts:
        out.update(d)
    return out

def load_build(build):
    name = list(build)[0]
    properties = {}
    for d in build[name]:
        properties.update(d)
    print(properties)

    # Preprocess properties
    sources = process(properties, 'sources')
    includes = process(properties, 'includes')
    libraries = process(properties, 'libraries')
    flags = process(properties, 'flags')

    return Build('example', name, sources, includes, libraries, flags)

def load_predefs(defs):
    for defn in defs:
        predefined.update(defn)

def load_builds(builds):
    blist = {}
    for b in builds:
        name = list(b)[0]
        build = load_build(b)
        blist.update({name: build})
    
    return blist

def load_target(target, blist):
    print('TARGET = ', target)
    name = list(target)[0]
    properties = {}
    for d in target[name]:
        properties.update(d)
    
    # Preprocess properties
    modes = process(properties, 'modes')

    # Gets builds and postexecs
    builds = concat(properties['builds'])
    postexecs = concat(properties['postexecs'])

    # Preprocess predefined things
    for b in builds:
        bname = builds[b]

        if bname in blist:
            builds[b] = blist[bname]
        # TODO: errir handling here
    

    # If the postexec is a string, then convert to Script
    for pe in postexecs:
        pname = postexecs[pe]

        if pname in predefined:
            postexecs[pe] = predefined[pname]
        else:
            postexecs[pe] = Script(pname)

    print(properties['builds'])
    print(modes, builds, postexecs)

    return Target(name, modes, builds, postexecs)

def load_targets(targets, blist):
    tlist = {}
    for t in targets:
        name = list(t)[0]
        target = load_target(t, blist)
        tlist.update({name: target})

    return tlist

def load_smake(file):
    with open(file, 'r') as file:
        smake = yaml.safe_load(file)

    load_predefs(smake['sources'])

    builds = smake['builds']
    builds = load_builds(builds)

    targets = smake['targets']
    targets = load_targets(targets, builds)
    return targets

builds = load_smake('example.yaml')
print(builds)
builds['mercury'].run()
import yaml

def load_smake(file):
    with open(file, 'r') as file:
        smake = yaml.safe_load(file)

    print(smake)

load_smake('example.yaml')

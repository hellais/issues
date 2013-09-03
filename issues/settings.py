import yaml

class Config(dict):
    def __init__(self, config_file='issues.conf'):
        with open(config_file) as f:
            c = yaml.load(f)
        for k,v in c.items():
            self[k] = v

config = Config()

import json
from os import path


class Config(dict):

    def __init__(self, filename='config.json', live=False):
        self.conf_file = filename
        self.live = live
        self.template = """{
            "token": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "main_guild": "xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "admin_roles": [0],
            "prefix": "alpha",
            "cheese_weight": 30
        }"""
        self.load()

    def __setitem__(self, key, value, /):
        """
        Override the setitem function to save after every alteration
        - self.live must be true
        """
        Changed = False
        if key in self.keys():
            Changed = self[key] != value
        if Changed:
            super().__setitem__(key, value)
            if self.live:
                self.save()

    def load(self):
        try:
            with open(self.conf_file) as conf:
                self.update(json.load(conf))
        except FileNotFoundError as e:
            self.update(json.loads(self.template))
            self.save()

    def save(self):
        with open(self.conf_file, 'w') as conf:
            json.dump(self.copy(), conf)

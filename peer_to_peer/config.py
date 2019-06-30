import json

class config_read():

    def __init__(self, config_file):
        self.data = {}
        with open(config_file) as json_file:
            self.data = json.load(json_file)

    def get_name(self):
        return self.data['config']['name']

    def get_ip(self):
        return self.data['config']['ip']

    def get_neighbors(self):
        return (self.data['config']['neighbors']).split(",")

    def get_port(self):
        return self.data['config']['port']

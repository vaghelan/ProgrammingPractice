import json

class config_read():

    def __init__(self, config_file):
        self.data = {}
        with open(config_file) as json_file:
            self.data = json.load(json_file)

        host_port_pairs = []

        if self.data['config']['neighbors'] != '':
            host_port_pairs = (self.data['config']['neighbors']).split(",")

        self.neighbors = []
        for hp in host_port_pairs:
            hp_set = hp.split(":")
            self.neighbors.append((hp_set[0].strip(), hp_set[1].strip()))

        print (self.neighbors)

    def get_name(self):
        return self.data['config']['name']

    def get_ip(self):
        return self.data['config']['ip']

    def get_neighbors(self):
        return self.neighbors

    def get_port(self):
        return self.data['config']['port']
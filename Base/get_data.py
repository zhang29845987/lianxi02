import os

import yaml


class Data:
    def ss(self, data_file):
        with open("./data" + os.sep + data_file, "r") as f:
            return yaml.safe_load(f)


import json


class ConfigManager():

    def __init__(self):
        try:
            with open("config/conf.json") as fin:
                conf = json.load(fin)
        except FileNotFoundError as e:
            print ("Config file not found")
            sys.exit(1)

        print conf
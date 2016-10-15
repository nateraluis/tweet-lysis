import os
import json
from datetime import datetime


class ConfigManager():

    def __init__(self):
        try:
            with open("config/conf.json") as fin:
                conf = json.load(fin)
        except FileNotFoundError as e:
            print ("Config file not found")
            sys.exit(1)

        self.TWEETS_PATH = self.createTweetsDir(conf['TWEETS_PATH'])
        self.DEBUG = conf['DEBUG']


    def createTweetsDir(self, PATH):
        dir_path = os.path.join(os.path.expanduser('~'), '.tweet-lysis', PATH)
        if not os.path.exists(dir_path):
            try:
                os.makedirs(dir_path)
            except OSError as e:
                print "Couldn't create the directory so store data"
                sys.exit(1)
        # Log here
        return dir_path

    def newQueryPath(self, query_term):
        query_timestamp = datetime.now().strftime("%y%m%d_%H:%M:%S")
        set_path = query_timestamp + "_" + query_term.replace(" ", "_")
        query_path = os.path.join(self.TWEETS_PATH, set_path + ".json")
        # Log here
        return query_path

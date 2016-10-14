#
# import sys
# import os
#
# import Auth
#
# path = os.path.dirname(os.path.abspath(__file__))
#
# TWEETS_PATH = Auth.getKey("config/meta.json")
#
# savepath = os.path.join(path, TWEETS_PATH, strftime("%m/%d", time.localtime()))
# filename = os.path.join(savepath, tweet_id + ".json")
#
# if not os.path.exists(savepath):
#     logging.info("Creating path: " + savepath)
#     os.makedirs(savepath)
# with open(filename, 'w') as fout:
#     json.dump(json_data, fout)

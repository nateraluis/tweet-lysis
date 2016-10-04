
from tweepy import TweepError
import tweepy
import time
import json
import logging
import sys

KEYFILE = "config/meta.json"

# Load the twitter keys
def get_key(keyfile):
	try:
		with open(keyfile) as fin:
			key = json.load(fin)
	except FileNotFoundError as e:
		print ("Key not found")
		sys.exit(1)
	return key

def process_status(count, status):
    out = "(%d) [%s] %s: %s" % (count, status.created_at, status.user.screen_name, status.text)
    return out

def main():
        key = get_key(KEYFILE)
    	auth = tweepy.OAuthHandler(key['consumer_key'], key['consumer_secret'])
    	auth.set_access_token(key['access_token'], key['access_secret'])
        api = tweepy.API(auth)

        # Only iterate through the first 200 statuses
        count = 1

        query_term = "#MAGA"

        tweets = tweepy.Cursor(
            api.search,
            q=query_term,
            result_type="recent",
            since="2016-09-27",
            until="2016-10-02",
            show_user=True
        ).items(100)

        while True:
            try:
                print process_status(count, tweets.next())
                print "--------------"
                print ""
                count += 1
            except TweepError:
                time.sleep(60 * 15)
                continue
            except StopIteration:
                break

if __name__ == "__main__":
    main()

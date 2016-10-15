import tweepy
import sys
import os

import json

# Load the twitter keys
def getKey(keyfile):
	try:
		with open(keyfile) as fin:
			key = json.load(fin)
	except FileNotFoundError as e:
		print "Exception found"
		sys.exit(1)
	# Log here
	return key

def getAPI():
	key_path = os.path.join(os.getcwd(), "config/meta.json")
	key = getKey(key_path)
	# create authentication handlers given pre-existing keys
	# auths = []
	# for key['consumer_key'], key['consumer_secret'], key['access_token'], key['access_secret'] in key:
	consumer_key = key['consumer_key']
	consumer_secret = key['consumer_secret']
	access_token = key['access_token']
	access_secret = key['access_secret']
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	    # auths.append(auth)

	# api = tweepy.API(auths)
	#
	# # switch to the second authentication handler (zero-based index)
	# api.auth_idx = 1

	return tweepy.API(auth)#, monitor_rate_limit=True, wait_on_rate_limit=True)

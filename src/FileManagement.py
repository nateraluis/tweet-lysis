from tweepy import TweepError

import sys
import os
import json

def saveTweetQuery(tweetQuery, queryPath):
    jsonQuery = []
    tweetsProcessed = 0
    while True:
        try:
            tweet = tweetQuery.next()
        except TweepError:
            print """
------------------------
        ERROR
------------------------
 Please wait 15 minutes
 Downloaded %d tweets
            """ % (tweetsProcessed)
            break
        except StopIteration:
            break
        tweetsProcessed += 1
        jsonQuery.append(tweet._json)


    # TODO DO NOT FUCKING FORGET TO TURN THIS ON!!!!
    # with open(queryPath, 'w') as query_file:
    #     json.dump(jsonQuery, query_file)


    return jsonQuery

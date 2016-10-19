from tweepy import TweepError

import sys
import os
import json

import Auth

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

def createCredentials(path):
    cons_key = raw_input('Enter the consumer key: ')
    cons_sec = raw_input('Enter the consumer secret: ')
    acc_tok = raw_input('Enter the access token: ')
    acc_sec = raw_input('Enter the access secret: ')

    # As long as credentials are not valid, ask for them
    while not Auth.__validateUser__(cons_key, cons_sec, acc_tok, acc_sec):
        print ""
        print "Error: The credentials provided are not valid"
        cons_key = raw_input('Enter the consumer key: ')
        cons_sec = raw_input('Enter the consumer secret: ')
        acc_tok = raw_input('Enter the access token: ')
        acc_sec = raw_input('Enter the access secret: ')
        print ""

    with open(path, 'w') as f:
        credentials = {
            "consumer_key": str(cons_key),
            "consumer_secret": str(cons_sec),
            "access_token": str(acc_tok),
            "access_secret": str(acc_sec)
        }
        json.dump(credentials, f)


    return "Success"

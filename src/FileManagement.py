
import sys
import os
import json

def saveTweetQuery(tweetQuery, queryPath):
    jsonQuery = []
    for tweet in tweetQuery:
        jsonQuery.append(tweet._json)
    return jsonQuery

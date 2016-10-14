
from collections import Counter

import config.ConfigManager as CM
import numpy as np
import json
import TweetProcess as TP

VERBOSE = True

def getUniqueHTList(HTList):
    return set(HTList)


def getAssociatedHashtags(tweets, original):
    HTList = []
    tweetsProcessed = 0

    for tweet in tweets:
        for hashtags in tweet['entities']['hashtags']:
            ht = hashtags[u'text'].lower()
            if ht != original.lower():
                HTList.append(ht)

    return HTList

def countHT(HTList):
    HTCount = []
    for ht in HTList:
        #ht count
        htc = (ht, HTList.count(ht))
        if not htc in HTCount:
            HTCount.append(htc)
    return HTCount


def getMostUsed(HTList, number):
    counter = Counter(HTList)
    return counter.most_common(number)

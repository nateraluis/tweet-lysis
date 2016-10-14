from tweepy import TweepError
from collections import Counter

import numpy as np
import json


def getAssociatedHashtags(tweets, original):
    HTList = []
    while True:
        try:
            status = tweets.next()
        except StopIteration:
            break
        for entity in status.entities['hashtags']:
            for element in entity[u'text'].splitlines():
                if element and element != original:
                    HTList.append(element.lower())
    # while end

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

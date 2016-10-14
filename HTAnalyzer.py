from tweepy import TweepError

import json


def getAssociatedHashtags(tweets):
    HTList = []
    while True:
        try:
            status = tweets.next()
        except StopIteration:
            break
        for entity in status.entities['hashtags']:
            for element in entity[u'text'].splitlines():
                if element:
                    HTList.append(element)
    # while end
    HTList = [ht.lower() for ht in HTList] # Lowercase the whole list
    return HTList

def countHT(HTList):
    HTCount = []
    for ht in HTList:
        #ht count
        htc = {ht: HTList.count(ht)}
        if not htc in HTCount:
            HTCount.append(htc)
    return HTCount

from tweepy import TweepError
from collections import Counter

import numpy as np
import json
import TweetProcess as TP

VERBOSE = True

def getUniqueHTList(HTList):
    return set(HTList)


def getAssociatedHashtags(tweets, original):
    HTList = []
    tweetsProcessed = 0
    while True:
        try:
            status = tweets.next()
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
            if VERBOSE:
                print "+++ End of cursor +++"
            break
        tweetsProcessed += 1
        TP.printTweet(status)
        for entity in status.entities['hashtags']:
            for element in entity[u'text'].splitlines():
                if element and element.lower() != original:
                    HTList.append(element.lower())
    if VERBOSE:
        print """
------------------------
        Finished
------------------------
 Successfully downloaded
 and processed %d tweets.
 Found %d associated HTs.
        """ % (tweetsProcessed, len(set(HTList)))
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

from tweepy import TweepError

import json


def printPocessed(status):
    out = "[%s] %s: %s" % (status.created_at, status.user.screen_name, status.text)
    return out

def printTweets(tweets):
    while True:
        try:
            # print printPocessed(tweets.next())
            print printOnlyAssociatedHashtags(tweets.next())
            print "--------------"
            print ""
        except TweepError:
            time.sleep(60 * 15)
            continue
        except StopIteration:
            break

def printOnlyAssociatedHashtags(status):
    for entity in status.entities['hashtags']:
        for element in entity[u'text'].splitlines():
            print element


def printList(HTList):
    for ht in HTList:
        print ht

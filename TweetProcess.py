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


# For "get hashtags"
#   extract tweets ht
#   add them to list
#   check for duplicates
#   write json
        # {
        #     "ht1": reps,
        #     "ht2": reps,
        #     "ht3": reps,
        # }

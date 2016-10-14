from tweepy import TweepError
from collections import Counter

import HTAnalyzer as HTA
import WordPreprocess as WP

import json


def printTweet(status):
    print "[%s] %s: %s" % (status.created_at, status.user.screen_name, status.text)
    print ""


def printTweets(tweets):
    while True:
        try:
            print printTweet(tweets.next())
            print "--------------"
            print ""
        except TweepError:
            time.sleep(60 * 15)
            continue
        except StopIteration:
            break

def printList(HTList):
    for ht in HTList:
        print ht

def countWordOccurrences(tweets, HTList):
    HTUniqueList = HTA.getUniqueHTList(HTList)
    wordsWithStop = []
    for tweet in tweets:
        text = tweet.text
        wordsWithStop += WP.preprocess(text, lowercase=True)

    words = [term for term in wordsWithStop if term not in WP.stopwords or HTList]

    counter = Counter(words)
    print counter.most_common(3)

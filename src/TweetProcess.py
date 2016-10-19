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

def countWordOccurrences(tweets, HTList, most_used=10):
    HTUniqueList = HTA.getUniqueHTList(HTList)
    wordsWithStop = []
    for tweet in tweets:
        wordsWithStop += WP.preprocess(tweet['text'], lowercase=True)

    words = [term for term in wordsWithStop
            if term not in WP.stop and
            not term.startswith(('#', '@'))]
    counter = Counter(words)

    mostUsed = counter.most_common(most_used)
    print "The most used words were:"
    for word in mostUsed:
        print "\t %s with %d occurrences" % (word[0], word[1])

    return mostUsed

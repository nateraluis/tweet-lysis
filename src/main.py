
import tweepy
import time
import json
import logging
import sys

import Auth
import TweetProcess as TP
import HTAnalyzer as HTA
import Plotter
import FileManagement as FM

import config.ConfigManager as CM


def main():
        api = Auth.getAPI()

        conf = CM.ConfigManager()

        query_term = "#MakeAmericaGreatAgain"

        tweets = tweepy.Cursor(
            api.search,
            q=query_term,
            result_type="recent",
            since="2016-10-13",
            until="2016-10-14",
            show_user=True
        ).items(2)

        query_dir = conf.newQueryPath(query_term)
        tweetsAsJSON = FM.saveTweetQuery(tweets, query_dir)
        for tweet in tweetsAsJSON:
            print tweet['user']['screen_name']
            print ""
            print "---------"
            print ""
        # print tweetsAsJSON


        # TP.printTweets(tweets)
        # HTList = HTA.getAssociatedHashtags(tweets, "MakeAmericaGreatAgain".lower())
        # TP.countWordOccurrences(tweets)#, HTList)

        # TODO not needed anymore
        # HTCount = HTA.countHT(HTList)


        # print HTA.getMostUsed(HTList, 3)
        # print HTCount
        # TP.printList(HTCount)

        # Plotter.plotAllRelatedHT(HTA.getMostUsed(HTList, 3))
        # Plotter.plotCountRelatedHT(HTA.getMostUsed(HTList, 10))



if __name__ == "__main__":
    main()

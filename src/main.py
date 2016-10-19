
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
        ).items(200)

        query_dir = conf.newQueryPath(query_term)
        # TODO Turn saving on
        tweetsAsJSON = FM.saveTweetQuery(tweets, query_dir)


        # TP.printTweets(tweets)
        HTList = HTA.getAssociatedHashtags(tweetsAsJSON, "MakeAmericaGreatAgain")
        # TP.printList(HTList)
        WordOccurrences = TP.countWordOccurrences(tweetsAsJSON, HTList)


        # print HTA.getMostUsed(HTList, 3)
        # print HTCount

        # Plotter.plotTupleCount(HTA.getMostUsed(HTList, 3))
        Plotter.plotTupleCount(WordOccurrences)
        # Plotter.plotTupleCount(HTA.getMostUsed(HTList, 2))



if __name__ == "__main__":
    main()

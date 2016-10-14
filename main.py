
import tweepy
import time
import json
import logging
import sys

import Auth
import TweetProcess as TP
import HTAnalyzer as HTA
import Plotter



def main():

        api = Auth.getAPI()

        # Only iterate through the first 200 statuses
        count = 1

        query_term = "#MakeAmericaGreatAgain"

        tweets = tweepy.Cursor(
            api.search,
            q=query_term,
            result_type="recent",
            since="2016-10-09 20:00",
            until="2016-10-09 22:00",
            show_user=True
        ).items(5000)

        # TP.printTweets(tweets)
        HTList = HTA.getAssociatedHashtags(tweets, "MakeAmericaGreatAgain".lower())
        HTCount = HTA.countHT(HTList)
        # print HTA.getMostUsed(HTList, 3)
        # print HTCount
        # TP.printList(HTCount)

        # Plotter.plotAllRelatedHT(HTA.getMostUsed(HTList, 3))
        Plotter.plotCountRelatedHT(HTA.getMostUsed(HTList, 10))



if __name__ == "__main__":
    main()

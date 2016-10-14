
import tweepy
import time
import json
import logging
import sys

import Auth
import TweetProcess as TP
import HTAnalyzer as HTA



def main():

        api = Auth.getAPI()

        # Only iterate through the first 200 statuses
        count = 1

        query_term = "#MakeAmericaGreatAgain"

        tweets = tweepy.Cursor(
            api.search,
            q=query_term,
            result_type="recent",
            since="2016-10-11",
            until="2016-10-13",
            show_user=True
        ).items(10)

        # TP.printTweets(tweets)
        HTList = HTA.getAssociatedHashtags(tweets)
        HTCount = HTA.countHT(HTList)
        TP.printList(HTCount)



if __name__ == "__main__":
    main()

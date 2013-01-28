"""
Copyright (c) 2013 Michael Markieta
See the file license.txt for copying permission.
"""
import json
import csv


def parse_tweets(tweet_file):
    """
    After retrieving the twitter json using a cURL request from Twitter, parse_tweets will accept the json and parse
    it for you to extract the date, time, PM2.5 reading, and locale.
    --------------------------------------------------------------------------------------------------------------------
    :param tweet_file:  JSON file created by cURL request using Twitter API
    :type tweet_file:   String
    --------------------------------------------------------------------------------------------------------------------
    Returns a structured list of list: pm_25 = [[locale, date_time, pm_25], [locale, date_time, pm_25], [..., ..., ...]]
    Note: All the air quality providers in China report hourly, but are not running on a 100% uptime, therefore take
    heed and you will notice that the time stamps generally won't line up.
    """

    tweets = []

    locale_dict = {15527964:"Beijing",
                   577897347:"Chengdu",
                   304788556:"Guangzhou",
                   562768872:"Shanghai"}

    for line in open(tweet_file):
        try:
            tweets.append(json.loads(line))
        except:
            pass

    texts = [tweet['text'] for tweet in tweets[0]]
    locale = [tweet['user']['id'] for tweet in tweets[0]]

    pm_25 = [["locale", "date_time", "pm_25"]]

    for _ in range(0, len(texts)):
        try:
            location = locale_dict[locale[-1]]
            date_time = texts[-1].rsplit(";")[0]
            pm_25_level = texts[-1].rsplit(";")[texts[-1].rsplit(";").index(" PM2.5") + 1].lstrip(" ")
            pm_25.insert(1,[location, date_time, pm_25_level])
        except:
            pass

        texts.pop()
        locale.pop()

    return pm_25


def write_to_csv(pm_25, output):
    """
    Use this function to write the parse_tweets result to a csv file for further manipulation.
    --------------------------------------------------------------------------------------------------------------------
    :param pm_25:   Output from parse_tweets function (list of lists)
    :type pm_25:    List
    :param output:  Location to save CSV file (format: "xyz.csv")
    :type output:   String
    """

    with open(output, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',')
        for row in pm_25:
            spamwriter.writerow(row)

    print "File processed: %s" % output

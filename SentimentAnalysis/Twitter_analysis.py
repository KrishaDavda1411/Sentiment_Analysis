# import GetOldTweets3 as got
#
# def get_tweets():
#     tweetCriteria = got.manager.TweetCriteria().setQuerySearch('corona') \
#         .setSince("2020-05-01") \
#         .setUntil("2021-09-30") \
#         .setMaxTweets(1)
#     tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]
#     print(tweet.text)
#
# get_tweets()

import tweepy
import configparser
#read configs
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['twitter']['api_key']
api_Key_Secret = config['twitter']['api_Key_Secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# print(access_token_secret)

#authentication
auth = tweepy.OAuthHandler(api_key,api_Key_Secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

words = input("key_words = ")
no = int(input("number = "))
tweet_from_keyword = tweepy.Cursor(api.search_tweets,q=words,lang="en",tweet_mode = 'extended').items(no)
list_tweet = [tweet for tweet in tweet_from_keyword]
print(list_tweet)
for tweet in list_tweet:
    des = tweet.user.description
    print(des)


public_tweet = api.home_timeline()
# public_tweet=tweet_from_keyword
# print(public_tweet[0].text)



# text_tweets=[]
# for tweets in public_tweet:
#     print((tweets.text))
#     text_tweets.append(tweets.text)
# print(text_tweets)
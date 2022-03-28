 # Cleaning text steps
# 1. create a txt file and take text from it
# 2. convert the letter in lowercase
# 3. remove punctuation like .,?

import string
from collections import Counter
import matplotlib.pyplot as plt
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
text_tweets=[]
for tweet in list_tweet:
    des = tweet.user.description
    text_tweets.append(des)
    print(des)


public_tweet = api.home_timeline()
# print(public_tweet[0].text)

'''for tweets in public_tweet:
    # print((tweets.text))
    text_tweets.append(tweets.text)
# print(text_tweets)

# text = open('read.txt',encoding='utf-8').read()'''
text = ''
length = len(text_tweets)

# print(string.punctuation)
# print(lower_case)
for i in range(0,length):
    text = text + text_tweets[i] + " "
lower_case = text.lower()

'''
str1: specifies list of char that need to be replaced
str2: specifies the list of char which the char need to be replaced
str3: specifies the list of char that need to be deleted
returns: returns the translation table which specifies the conversions that can be used  
'''
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
# print(cleaned_text)

tokenized_words = cleaned_text.split()
# print(tokenized_words)

#stop words does not add any emotional meaning to stmt like i , was, that
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []
for i in tokenized_words:
    if i not in stop_words:
        final_words.append(i)
# print(final_words)

emotion_list = []
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace('\n','').replace(',','').replace("'",'').strip()
        # print(clear_line)
        word,emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

# print(emotion_list)

w = Counter(emotion_list)
print(w)

fig , ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
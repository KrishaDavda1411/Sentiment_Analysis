 # Cleaning text steps
# 1. create a txt file and take text from it
# 2. convert the letter in lowercase
# 3. remove punctuation like .,?

import string
from nltk.corpus import  stopwords
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt

text = open('read.txt',encoding='utf-8').read()
lower_case = text.lower()
# print(string.punctuation)
# print(lower_case)


'''
str1: specifies list of char that need to be replaced
str2: specifies the list of char which the char need to be replaced
str3: specifies the list of char that need to be deleted
returns: returns the translation table which specifies the conversions that can be used  
'''
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
# print(cleaned_text)

tokenized_words = word_tokenize(cleaned_text,"english")
#when read.txt is very big then .split take more time so we are using word_tokenize
# print(tokenized_words)

#stop words does not add any emotional meaning to stmt like i , was, that

final_words = []
for i in tokenized_words:
    if i not in stopwords.words('english'):
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

print(emotion_list)

w = Counter(emotion_list)
print(w)

def sentiment_analyze(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    pos = score['pos']
    if neg>pos:
        print("negative sentiment")
    elif pos>neg:
        print("positive sentiment")
    else:
        print("neutral vibe")
    # print(score)

sentiment_analyze(cleaned_text)


fig , ax1 = plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
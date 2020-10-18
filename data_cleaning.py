# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 01:15:17 2020

@author: Arthur Chu
"""

import pandas as pd
import re
#from nltk.corpus import stopwords

df = pd.read_csv('all_tweets.csv')

#STOPWORDS = set(stopwords.words('english'))

replace_by_space_re = re.compile('[/(){}\[\]\|@,;]')

bad_symbols_re = re.compile('[^0-9a-z #+_]')


#drop unnecessary columns of data

#df.drop(['user_id', 'tweet_id', 'tweet_url', 'timestamp',
#         'timestamp_epochs', 'text_html', 'img_urls', 'video_url', 
#         'is_replied', 'is_reply_to', 'parent_tweet_id', 
#         'reply_to_users'], axis = 1, inplace = True)
#keeping duplicates as they might be reweets of one another
#parse website link for website posted(drop bit.ly)
df['links'] = df['links'].apply(lambda x: x.split('//')[-1].split('/')[0])

df['text'] = df['text'].str.lower()
df.hashtags = df.hashtags.str.lower()

#df['text'].replace_by_space_re.sub('', df['text'])
#df['text'].bad_symbols_re.sub('', df['text'])

df.to_csv('all_tweets.csv', index = False)
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 01:15:17 2020

@author: Arthur Chu
"""

import pandas as pd

df = pd.read_csv('all_tweets.csv')

#drop unnecessary columns of data

df.drop(['user_id', 'tweet_id', 'tweet_url', 'timestamp',
         'timestamp_epochs', 'text_html', 'img_urls', 'video_url', 
         'is_replied', 'is_reply_to', 'parent_tweet_id', 
         'reply_to_users'], axis = 1, inplace = True)
#keeping duplicates as they might be reweets of one another
#parse website link for website posted(drop bit.ly)
df['links'] = df['links'].apply(lambda x: x.split('//')[-1].split('/')[0])


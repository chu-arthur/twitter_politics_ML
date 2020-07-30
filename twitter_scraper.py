# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 01:46:37 2020

@author: Arthur Chu
"""

from twitterscraper import query_tweets_from_user
import pandas as pd

tweets = []

twitter_handle_file_path = r"C:\Users\Arthur Chu\Desktop\twitter_politics_ML\raw_data\congress_twitter_handles.csv"

twitter_handles = pd.read_csv(twitter_handle_file_path, encoding = "ISO-8859-1")

twitter_handles.dropna(how = "any", inplace = True)

handles = twitter_handles['Twitter Handle'].tolist()

for politician in handles:
    tweets+= query_tweets_from_user(politician, limit = 1000)
    
df = pd.DataFrame(t.__dict__ for t in tweets)

df.to_csv(r"C:\Users\Arthur Chu\Desktop\twitter_politics_ML\raw_data\all_tweets.csv", index = False)

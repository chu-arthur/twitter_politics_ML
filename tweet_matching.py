# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 23:23:07 2020

@author: Arthur Chu
"""

import pandas as pd

tweets = pd.read_csv('all_tweets.csv')
scores = pd.read_csv('clean_ideology_scores.csv')

scores['Twitter Handle'] = scores['Twitter Handle'].str.replace(r'@', '')

complete_dataset = pd.merge(tweets, scores, how="left", left_on = "screen_name", right_on = "Twitter Handle")

complete_dataset.drop('Twitter Handle', inplace = True, axis = 1)
complete_dataset['ideology'].interpolate(inplace = True)

complete_dataset.fillna(method = 'ffill', inplace = True)

complete_dataset.to_csv('complete_dataset.csv')
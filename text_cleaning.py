# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 00:10:04 2020

@author: Arthur Chu
"""

import pandas as pd
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import defaultdict
from nltk.corpus import wordnet as wn

dataset = pd.read_csv('complete_dataset.csv')
dataset['text'] = [entry.lower() for entry in dataset['text']]

dataset['text'] = [word_tokenize(entry) for entry in dataset['text']]

tag_map = defaultdict(lambda : wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV


for index, entry in enumerate (dataset['text']):
    Final_words = []
    word_Lemmatized = WordNetLemmatizer()
    for word, tag in pos_tag(entry):
        if word not in stopwords.words('english') and word.isalpha():
            word_Final = word_Lemmatized.lemmatize(word,tag_map[tag[0]])
            Final_words.append(word_Final)
    dataset.loc[index, 'text_final'] = str(Final_words)


dataset.drop(['text', 'links', 'hashtags', 'has_media', 'likes', 'retweets', 'replies', 'screen_name', 'username'], inplace = True, axis = 1)

dataset['ideology_type'] = dataset['ideology'].apply(lambda x: 1 if x > 0.5 else 0)
dataset.drop(dataset.columns[0], axis = 1)
dataset.to_csv('complete_dataset.csv')

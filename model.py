# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 22:31:37 2020

@author: Arthur Chu
"""

import pandas as pd
import time
from sklearn import svm
from sklearn.metrics import classification_report

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

data = pd.read_csv('complete_dataset.csv')

data = data.loc[:, ['text_final', 'ideology_type']]

train, test = train_test_split(data, test_size = 0.35, random_state = 1)
X_train = train['text_final'].values
X_test = test['text_final'].values
y_train = train['ideology_type']
y_test = test['ideology_type']

vectorizer = TfidfVectorizer(min_df = 3, max_df = 0.65, sublinear_tf = True, use_idf = True)

train_vectors = vectorizer.fit_transform(X_train)
test_vectors = vectorizer.transform(X_test)

classifier_linear = svm.SVC(kernel = 'linear')
t0 = time.time()
classifier_linear.fit(train_vectors, y_train)
t1 = time.time()
prediction_linear = classifier_linear.predict(test_vectors)
t2 = time.time()
time_linear_train = t1-t0
time_linear_predict = t2-t1

print("Training time: %fs; Prediction time: %fs" %(time_linear_train, time_linear_predict))

report = classification_report(y_test, prediction_linear, output_dict = True)

print('Conservative: ', report['1'])
print('Liberal: ', report['0'])




tweet = "The GOP gave a $150 billion tax giveaway to the wealthiest in America, but now claim we cannot afford to provide expanded benefits for the unemployed. The GOP needs to get serious & work with Democrats to come to an agreement that helps working families."

tweet_vector = vectorizer.transform([tweet])

print(classifier_linear.predict(tweet_vector))


import pickle

pickle.dump(vectorizer, open('vectorizer.sav', 'wb'))
pickle.dump(classifier_linear, open('classifier.sav', 'wb'))
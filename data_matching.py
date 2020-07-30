# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 04:12:55 2020

@author: Arthur Chu
"""

import pandas as pd

handles = pd.read_csv('congress_twitter_handles.csv', encoding = 'ISO-8859-1')

handles.loc[handles['State'] == 'MN-8', ['State']] = 'MN-08'

handles.loc[handles['State'] == 'MO-2', ['State']] = 'MO-02'

handles["last_name"] = handles['Name'].str.rsplit(" ", 1).str[-1]

for i in range(436, 536):
    handles.loc[i, 'State'] += " " + handles.loc[i, 'last_name']

house_scores = pd.read_csv('house_ideology_score_2019.csv')

senate_scores = pd.read_csv('senate_ideology_score_2019.csv')

house_scores.drop('bioguide_id', axis = 1, inplace = True)

house_scores["ref"] = house_scores["state"] + '-'+house_scores["district"].astype(int).astype(str).str.zfill(2)

house_scores.loc[house_scores['ref'] == 'DC-00', ['ref']] = 'DC Delegate'

house_scores.loc[house_scores['ref'] == 'AK-00', ['ref']] = 'AK - At Large'

house_scores.loc[house_scores['ref'] == 'DE-00', ['ref']] = 'DE - At Large'

house_scores.loc[house_scores['ref'] == 'MT-00', ['ref']] = 'MT - At Large'

house_scores.loc[house_scores['ref'] == 'ND-00', ['ref']] = 'ND - At Large'

house_scores.loc[house_scores['ref'] == 'SD-00', ['ref']] = 'SD - At Large'

house_scores.loc[house_scores['ref'] == 'VT-00', ['ref']] = 'VT - At Large'

house_scores.loc[house_scores['ref'] == 'WY-00', ['ref']] = 'WY - At Large'


senate_scores.drop('bioguide_id', axis = 1, inplace = True)

senate_scores["ref"] = senate_scores["state"] + ' ' + senate_scores["name"]

congress_scores = pd.concat([house_scores, senate_scores])

ree = pd.merge(congress_scores, handles, left_on = 'ref', right_on = 'State')
## 1. Introduction to the Data ##

import pandas as pd
nba = pd.read_csv("nba_2013.csv")

# The names of the columns in the data
print(nba.columns.values)

## 3. Finding Similar Rows With Euclidean Distance ##

import math
selected_player = nba[nba["player"] == "LeBron James"].iloc[0]
distance_columns = ['age', 'g', 'gs', 'mp', 'fg', 'fga', 'fg.', 'x3p', 'x3pa', 'x3p.', 'x2p', 'x2pa', 'x2p.', 'efg.', 'ft', 'fta', 'ft.', 'orb', 'drb', 'trb', 'ast', 'stl', 'blk', 'tov', 'pf', 'pts']

def cal_dis(row):
    dis = 0
    for col in distance_columns:
        dis += (row[col] - selected_player[col])**2
    dis = math.sqrt(dis)
    return dis
lebron_distance = nba.apply(cal_dis,axis=1)

## 4. Normalizing Columns ##

nba_numeric = nba[distance_columns]
nba_normalized = (nba_numeric-nba_numeric.mean())/nba_numeric.std()

## 5. Finding the Nearest Neighbor ##

from scipy.spatial import distance

# Fill in the NA values in nba_normalized
nba_normalized.fillna(0, inplace=True)

# Find the normalized vector for Lebron James
lebron_normalized = nba_normalized[nba["player"] == "LeBron James"]

# Find the distance between Lebron James and everyone else.
euclidean_distances = nba_normalized.apply(lambda row: distance.euclidean(row, lebron_normalized), axis=1)
distance_frame = pandas.DataFrame(data={'dist':euclidean_distances, 'idx':euclidean_distances.index})
distance_frame.sort_values('dist',inplace=True)
index = distance_frame.iloc[1]['idx']
most_similar_to_lebron = nba.loc[int(index)]['player']

## 8. Computing Error ##

actual = test[y_column]
mse = ((actual - predictions)**2).sum()/len(actual)

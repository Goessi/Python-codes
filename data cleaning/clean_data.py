## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()
true_avengers = avengers[avengers['Year']> 1960]
        

## 5. Consolidating Deaths ##

def cal_deaths(row):
    cols = ['Death1','Death2','Death3','Death4','Death5']
    d = 0
    for c in cols:
        if row[c] == 'YES':
            d += 1
    return d
true_avengers['Deaths'] = true_avengers.apply(cal_deaths,axis =1)

## 6. Verifying Years Since Joining ##

joined_accuracy_count  = int()

def trueYear(row):
    year = 2015 - row['Year']
    if year == row['Years since joining']:
        a = 1
    return a
true_avengers['accurate'] = true_avengers.apply(trueYear,axis = 1)
joined_accuracy_count = sum(true_avengers['accurate'])

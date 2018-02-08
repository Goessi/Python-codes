## 2. Introduction to the Data ##

import pandas as pd
all_ages = pd.read_csv('all-ages.csv')
recent_grads = pd.read_csv('recent-grads.csv')
print(all_ages.head(5))
print(recent_grads.head(5))

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()


major = all_ages['Major_category'].unique()
for ma in major:
    rows = all_ages[all_ages['Major_category'] == ma]
    sum_rows = rows['Total'].sum()
    aa_cat_counts[ma] = sum_rows
    
major = recent_grads['Major_category'].unique()
for na in major:
    rows = recent_grads[recent_grads['Major_category'] == na]
    sum_rows = rows['Total'].sum()
    rg_cat_counts[na] = sum_rows

## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0
low_wage_proportion = recent_grads['Low_wage_jobs'].sum()/recent_grads['Total'].sum()

## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0

for item in majors:
    row_ag = all_ages[all_ages["Major"] == item]
    row_ag = row_ag.iloc[0]['Unemployment_rate']
    row_rg = recent_grads[recent_grads["Major"] == item]
    row_rg = row_rg.iloc[0]['Unemployment_rate']
    if row_rg < row_ag:
        rg_lower_count += 1
print(rg_lower_count)
    
# by summarizing different data, we could hace an initial impact about data

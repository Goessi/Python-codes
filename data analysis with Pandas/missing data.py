## 2. Introduction ##

import pandas as pd
titanic_survival = pd.read_csv('titanic_survival.csv')

## 3. Finding the Missing Data ##

age = titanic_survival["age"]
print(age.loc[10:20])
null_age = pandas.isnull(age)
age_null_true = age[null_age]
age_null_count = len(age_null_true)
print(age_null_count)

## 4. Whats the big deal with missing data? ##

# cannot compute mean for null value

age_is_null = pd.isnull(titanic_survival["age"])
age_not_null = titanic_survival['age'][age_is_null == False]
correct_mean_age = sum(age_not_null)/len(age_not_null)


## 5. Easier Ways to Do Math ##

correct_mean_age = titanic_survival["age"].mean()
correct_mean_fare = titanic_survival['fare'].mean()

## 6. Calculating Summary Statistics ##

passenger_classes = [1, 2, 3]
fares_by_class = {}
for cla in passenger_classes:
    rows = titanic_survival[titanic_survival['pclass'] == cla]
    fare = rows['fare']
    mean = fare.mean()
    fares_by_class[cla] = mean

## 7. Making Pivot Tables ##

import numpy as np
passenger_survival = titanic_survival.pivot_table(index="pclass", values="survived")
passenger_age = titanic_survival.pivot_table(index = 'pclass',values = 'age')
print(passenger_age)

## 8. More Complex Pivot Tables ##

import numpy as np
port_stats = titanic_survival.pivot_table(index = 'embarked', values = ['fare','survived'], aggfunc = np.sum)

## 9. Drop Missing Values ##

drop_na_rows = titanic_survival.dropna(axis=0)
drop_na_columns = titanic_survival.dropna(axis = 1)
new_titanic_survival = titanic_survival.dropna(axis = 0, subset = ['age','sex'])

## 10. Using iloc to Access Rows by Position ##

first_five_rows = new_titanic_survival.iloc[0:5]
first_ten_rows = new_titanic_survival.iloc[0:10]
row_position_fifth = new_titanic_survival.iloc[4]
row_index_25 = new_titanic_survival.loc[25]

## 11. Using Column Indexes ##

first_row_first_column = new_titanic_survival.iloc[0,0]
all_rows_first_three_columns = new_titanic_survival.iloc[:,0:3]
row_index_83_age = new_titanic_survival.loc[83,"age"]
row_index_766_pclass = new_titanic_survival.loc[766,"pclass"]

row_index_1100_age = new_titanic_survival.loc[1100,'age']
row_index_25_survived = new_titanic_survival.loc[25,'survived']
five_rows_three_cols = new_titanic_survival.iloc[0:5,0:3]

## 12. Reindexing Rows ##

# usually, we create a new column contains new index, if we don't want to the old index to exists, use drop=True

titanic_reindexed = new_titanic_survival.reset_index(drop = True)
print(titanic_reindexed.iloc[0:5,0:3])

## 13. Apply Functions Over a DataFrame ##

def hundredth_row(column):
    hundredth_item = column.iloc[99]
    return hundredth_item

hundredth_row_var = titanic_survival.apply(hundredth_row)

def count_null(column):
    col_is_null = column.isnull()
    col_null = column[col_is_null]
    num = len(col_null)
    return num

column_null_count = titanic_survival.apply(count_null)

## 14. Applying a Function to a Row ##

def is_minor(row):
    if row["age"] < 18:
        return True
    else:
        return False

minors = titanic_survival.apply(is_minor, axis=1)

def type_man(row):
    age = row['age']
    if pd.isnull(age):
        return 'unknown'
    elif age < 18:
        return 'minor'
    else:
        return 'adult'
    
age_labels = titanic_survival.apply(type_man,axis = 1)

## 15. Calculating Survival Percentage by Age Group ##

age_group_survival = titanic_survival.pivot_table(index = 'age_labels', values = 'survived')

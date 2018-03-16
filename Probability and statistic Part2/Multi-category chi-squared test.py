## 2. Calculating expected values ##

males_over50k = 0.241*0.669*32561
males_under50k = 0.759*0.669*32561
females_over50k = 0.241*0.331*32561
females_under50k = 0.759*0.331*32561

## 3. Calculating chi-squared ##

# 5249.8 2597.4 16533.5 8180.3
chisq_gender_income = (6662 - 5249.8)**2/5249.8 + (1179 - 2597.4)**2/2597.4 + (16533.5 - 15128)**2/16533.5 + (9592 - 8180.3)**2/8180.3

## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare

expected = np.array([5249.8,2597.4,16533.5,8180.3])
observed = np.array([6662,1179,15128,9592])
chi,pvalue_gender_income = chisquare(observed,expected)

## 5. Cross tables ##

import pandas
table = pandas.crosstab(income["sex"],[income["race"]])
print(table)

## 6. Finding expected values ##

import pandas
from scipy.stats import chi2_contingency
table = pandas.crosstab(income['sex'],[income['race']])
chi,pvalue_gender_race,df,ef = chi2_contingency(table)

## 1. Introduction ##

import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")

fig = plt.figure(figsize = (5,12))
ax1 = fig.add_subplot(4,1,1)
ax2 = fig.add_subplot(4,1,2)
ax3 = fig.add_subplot(4,1,3)
ax4 = fig.add_subplot(4,1,4)

ax1.set_xlim(0.0,5.0)
ax2.set_xlim(0.0,5.0)
ax3.set_xlim(0.0,5.0)
ax4.set_xlim(0.0,5.0)

movie_reviews['RT_user_norm'].hist(ax=ax1)
movie_reviews['Metacritic_user_nom'].hist(ax=ax2)
movie_reviews['Fandango_Ratingvalue'].hist(ax=ax3)
movie_reviews['IMDB_norm'].hist(ax=ax4)

## 2. Mean ##

def calc_mean(series):
    haha = series.values
    mean = sum(haha)/len(haha)
    return mean
cols = ['RT_user_norm','Metacritic_user_nom','Fandango_Ratingvalue','IMDB_norm']
user_reviews = movie_reviews[cols]
mean = user_reviews.apply(calc_mean)
rt_mean = mean['RT_user_norm']
mc_mean = mean['Metacritic_user_nom']
fg_mean = mean['Fandango_Ratingvalue']
id_mean = mean['IMDB_norm']


## 3. Variance and standard deviation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    vals = series.values
    mean = calc_mean(series)
    var = [v - mean for v in vals]
    sum_var = sum([v**2 for v in var])
    var = sum_var/len(vals)
    return var

rt_var = calc_variance(user_reviews['RT_user_norm'])
rt_stdev = rt_var**(1/2)

mc_var = calc_variance(user_reviews['Metacritic_user_nom'])
mc_stdev = mc_var**(1/2)

fg_var = calc_variance(user_reviews['Fandango_Ratingvalue'])
fg_stdev = fg_var**(1/2)

id_var = calc_variance(user_reviews['IMDB_norm'])
id_stdev = id_var**(1/2)

## 4. Scatter plots ##

fig = plt.figure(figsize = (4,8))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.set_xlim(0,5)
ax2.set_xlim(0,5)
ax3.set_xlim(0,5)

ax1.scatter(user_reviews['RT_user_norm'],user_reviews['Fandango_Ratingvalue'])
ax2.scatter(user_reviews['Metacritic_user_nom'],user_reviews['Fandango_Ratingvalue'])
ax3.scatter(user_reviews['IMDB_norm'],user_reviews['Fandango_Ratingvalue'])

## 5. Covariance ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_covariance(x_series,y_series):
    x_vals = x_series.values
    y_vals = y_series.values
    x_mean = calc_mean(x_series)
    y_mean = calc_mean(y_series)
    ss = 0
    for i in range(0,len(x_vals)):
        x = x_vals[i] - x_mean
        y = y_vals[i] - y_mean
        s = x*y
        ss = ss + s
    return ss/len(x_vals)

rt_fg_covar = calc_covariance(movie_reviews['RT_user_norm'],movie_reviews['Fandango_Ratingvalue'])
mc_fg_covar = calc_covariance(movie_reviews['Metacritic_user_nom'],movie_reviews['Fandango_Ratingvalue'])
id_fg_covar= calc_covariance(movie_reviews['IMDB_norm'],movie_reviews['Fandango_Ratingvalue'])

## 6. Correlation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

def calc_correlation(series1,series2):
    cov = calc_covariance(series1,series2)
    std1 = calc_variance(series1)**(1/2)
    std2 = calc_variance(series2)**(1/2)
    return cov/(std1*std2)

rt_fg_corr = calc_correlation(movie_reviews['RT_user_norm'],movie_reviews['Fandango_Ratingvalue'])
mc_fg_corr = calc_correlation(movie_reviews['Metacritic_user_nom'],movie_reviews['Fandango_Ratingvalue'])
id_fg_corr = calc_correlation(movie_reviews['IMDB_norm'],movie_reviews['Fandango_Ratingvalue'])
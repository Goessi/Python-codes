## 3. Bikesharing distribution ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")
num = bikes[bikes['cnt'] > 5000].shape[0]
total = bikes.shape[0]
prob_over_5000 = num/total

## 4. Computing the distribution ##

import math

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))
import math
def pro(p,k,N):
    if k != N:
        q = 1 - p
        times = math.factorial(N)/(math.factorial(k)*math.factorial(N-k))
        po = times*p**k*q**(N-k)
    else:
        po = p**k
    return po
outcome_probs = []
for i in range(31):
    po = pro(0.39,outcome_counts[i],30)
    outcome_probs.append(po)
    

## 5. Plotting the distribution ##

import matplotlib.pyplot as plt

# The most likely number of days is between 10 and 15.
plt.bar(outcome_counts, outcome_probs)
plt.show()

## 6. Simplifying the computation ##

import scipy
from scipy import linspace
from scipy.stats import binom
import matplotlib.pyplot as plt
# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)
haha = binom.pmf(outcome_counts,30,0.39)
plt.bar(outcome_counts,haha)
plt.show()

## 8. Computing the mean of a probability distribution ##

dist_mean = None
dist_mean = 30*0.39

## 9. Computing the standard deviation ##

dist_stdev = None
dist_stdev = (30*0.39*(1-0.39))**0.5

## 10. A different plot ##

import scipy
from scipy import linspace
from scipy.stats import binom
import matplotlib.pyplot as plt 
outcome_counts = linspace(0,10,11)
haha = binom.pmf(outcome_counts,10,0.39)
plt.bar(outcome_counts,haha)
plt.show()
outcome_counts = linspace(0,100,101)
xixi = binom.pmf(outcome_counts,100,0.39)
plt.bar(outcome_counts,xixi)
plt.show()

## 11. The normal distribution ##

# Create a range of numbers from 0 to 100, with 101 elements (each number has one entry).
outcome_counts = scipy.linspace(0,100,101)

# Create a probability mass function along the outcome_counts.
outcome_probs = binom.pmf(outcome_counts,100,0.39)

# Plot a line, not a bar chart.
plt.plot(outcome_counts, outcome_probs)
plt.show()

## 12. Cumulative density function ##

outcome_counts = linspace(0,30,31)
import scipy
from scipy.stats import binom
import matplotlib.pyplot as plt
dist = binom.cdf(outcome_counts,30,.39)
plt.plot(outcome_counts,dist)
plt.show()

## 14. Faster way to calculate likelihood ##

left_16 = None
right_16 = None

import scipy
from scipy import linspace
from scipy.stats import binom

haha = binom.cdf(16,30,0.39)
left_16 = haha

xixi = binom.cdf(16,30,0.39)
right_16 = 1 - xixi

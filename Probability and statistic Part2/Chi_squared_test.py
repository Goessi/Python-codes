## 2. Calculating differences ##

female_diff = (10771 - 16280.5)/16280.5
male_diff = (21790 - 16280.5)/16280.5

## 3. Updating the formula ##

female_diff = (10771 - 16280.5)**2/16280.5
male_diff = (21790 - 16280.5)**2/16280.5
gender_chisq = male_diff + female_diff

## 4. Generating a distribution ##

chi_squared_values = []
for i in range(0,1000):
    random_num = numpy.random.random(32561,)
    se_0 = random_num[random_num < 0.5]
    se_1 = random_num[random_num >= 0.5]
    count_0 = len(se_0)
    count_1 = len(se_1)    
    male_diff = (count_0 - 16280.5)**2/16280.5
    female_diff = (count_1 - 16280.5)**2/16280.5
    chi = male_diff + female_diff
    chi_squared_values.append(chi)
    
plt.hist(chi_squared_values)
plt.show()

## 6. Smaller samples ##

female_diff = (107.71 - 162.805)**2/162.805
male_diff = (217.9 - 162.805)**2/162.805
gender_chisq = female_diff + male_diff

## 7. Sampling distribution equality ##

chi_squared_values = []
for i in range(0,1000):
    v_300 = numpy.random.random(300,)
    ch_0 = v_300[v_300 < 0.5]
    ch_1 = v_300[v_300 >= 0.5]
    count_0 = len(ch_0)
    count_1 = len(ch_1)
    male_diff = (count_0 - 150)**2/150
    female_diff = (count_1 - 150)**2/150
    chi = male_diff + female_diff
    chi_squared_values.append(chi)
plt.hist(chi_squared_values)
plt.show()

## 9. Increasing degrees of freedom ##

diff_w = (27816 - 26146.5)**2/26146.5
diff_b = (3124 - 3939.9)**2/3939.9
diff_a = (1039 - 944.3)**2/944.3
diff_ai = (311 - 260.5)**2/260.5
diff_o = (271 - 1269.8)**2/1269.8
list_diff = [diff_w,diff_b,diff_a,diff_ai,diff_o]
race_chisq = sum(list_diff)

## 10. Using SciPy ##

from scipy.stats import chisquare
import numpy as np
observed = [27816,3124,1039,311,271]
expected = [26146.5,3939.9,944.3,260.5,1269.8]
chi,race_pvalue = chisquare(observed,expected)

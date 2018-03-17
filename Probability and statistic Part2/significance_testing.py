## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt
mean_group_a = np.mean(weight_lost_a)
print(mean_group_a)
mean_group_b = np.mean(weight_lost_b)
print(mean_group_b)
plt.hist(weight_lost_a)
plt.show()
plt.hist(weight_lost_b)
plt.show()

## 4. Test statistic ##

mean_difference = mean_group_b - mean_group_a
print(mean_difference)

## 5. Permutation test ##

import numpy as np
mean_difference = 2.52
print(all_values)
mean_differences = []
for i in range(0,1000):
    group_a = []
    group_b = []
    for v in all_values:
        random_num = np.random.rand(1,1)
        if random_num >= 0.5:
            group_a.append(v)
        else:
            group_b.append(v)
    mean_a = np.mean(group_a)
    mean_b = np.mean(group_b)
    iteration_mean_difference = mean_b - mean_a
    mean_differences.append(iteration_mean_difference)
plt.hist(mean_differences)
plt.show()
    

## 7. Dictionary representation of a distribution ##

sampling_distribution = {}
for v in mean_differences:
    if sampling_distribution.get(v,False):
        sampling_distribution[v] = sampling_distribution[v] + 1
        
    else:
        sampling_distribution[v] = 1

## 8. P value ##

frequencies = []
for k in sampling_distribution.keys():
    if abs(k) >= 2.52:
        frequencies.append(sampling_distribution[k])
    
p_value = sum(frequencies)/1000

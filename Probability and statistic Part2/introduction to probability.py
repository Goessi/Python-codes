## 1. Probability basics ##

# Print the first two rows of the data.
print(flags[:2])
most_bars_country = flags['name'][flags['bars'].idxmax()]
highest_population_country = flags['name'][flags['population'].idxmax()]

## 2. Calculating probability ##

total_countries = flags.shape[0]
count1 = 0
count2 = 0
for i in flags['orange']:
    if i == 1:
        count1 += 1
for i in flags['stripes']:
    if i > 1:
        count2 += 1
orange_probability = count1/total_countries
stripe_probability = count2/total_countries

    

## 3. Conjunctive probabilities ##

five_heads = .5 ** 5
ten_heads = .5**10
hundred_heads = .5**100

## 4. Dependent probabilities ##

red_flag = flags[flags['red'] == 1].shape[0]
total_countries = flags.shape[0]
three_red = red_flag*(red_flag - 1)*(red_flag - 2)/(total_countries*(total_countries - 1)*(total_countries - 2))

## 5. Disjunctive probability ##

start = 1
end = 18000
hundred_prob = 18000/100/18000
count = 0
for i in range(start,end):
    if i%70 == 0:
        count += 1
seventy_prob = count/end

## 6. Disjunctive dependent probabilities ##

stripes_or_bars = None
red_or_orange = None
red = flags[flags['red'] == 1].shape[0]
orange = flags[flags['orange'] == 1].shape[0]
r_n_o = flags[(flags['red'] == 1) & (flags['orange'] == 1)].shape[0]
red_or_orange = (red+orange-r_n_o)/flags.shape[0]

stripes = flags[flags['stripes'] >= 1].shape[0]
bars = flags[flags['bars'] >= 1].shape[0]
s_n_b = flags[(flags['stripes'] >= 1) & (flags['bars'] >= 1)].shape[0]
stripes_or_bars = (stripes + bars - s_n_b)/flags.shape[0]
        

## 7. Disjunctive probabilities with multiple conditions ##

heads_or = None
heads_or = 1 - 0.5**3

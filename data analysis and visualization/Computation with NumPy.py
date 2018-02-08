## 2. Array Comparisons ##

# return boolean datatype

countries_canada = (world_alcohol[:,2] == 'Canada')
years_1984 = (world_alcohol[:,0] == '1984')

## 3. Selecting Elements ##

country_is_algeria = (world_alcohol[:,2] == 'Algeria')
country_algeria = world_alcohol[country_is_algeria,:]

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = (world_alcohol[:,0] == '1986')&(world_alcohol[:,2] == 'Algeria')
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]

## 5. Replacing Values ##

world_alcohol_test = world_alcohol[:,0] == '1986'
world_alcohol[world_alcohol_test,0] = '2014'
a = world_alcohol[:,3] == 'Wine'
world_alcohol[a,3] = 'Grog'

## 6. Replacing Empty Strings ##

is_value_empty = world_alcohol[:,4] == ''
world_alcohol[is_value_empty,4] = 0

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:,4]
alcohol_consumption = alcohol_consumption.astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

is_canada_1986 = (world_alcohol[:,0] == '1986')&(world_alcohol[:,2] == 'Canada')
canada_1986 = world_alcohol[is_canada_1986,:]
canada_alcohol= canada_1986[:,4]
is_canada_1986_empty = canada_alcohol == ''
canada_alcohol[is_canada_1986_empty] = '0'
canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()

## 10. Calculating Consumption for Each Country ##

totals = {}
is_year = world_alcohol[:,0] == '1989'
year = world_alcohol[is_year,:]
        
for country in countries:
    is_country = year[:,2] == country
    country_consumption = year[is_country,:]
    is_empty = country_consumption[:,4]
    is_is_empty = is_empty == ''
    is_empty[is_is_empty] = '0'
    empty_zero = is_empty.astype(float)
    sum_of_country = empty_zero.sum()
    totals[country] = sum_of_country
    

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None
for key,value in totals.items():
    if value > highest_value:
        highest_value = value
        highest_key = key
       
        

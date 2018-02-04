## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i,item in enumerate(ships):
    print(item)
    print(cars[i])
    

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
for i, item in enumerate(things):
    item.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [app*2 for app in apple_prices]
apple_prices_lowered = [(app - 100) for app in apple_prices]

## 5. Counting Female Names ##

name_counts = {}
for row in legislators:
    if row[3] == 'F' and row[7] > 1940:
        name = row[1]
        if name in name_counts:
            name_counts[name] = name_counts[name] + 1
        if name not in name_counts:
            name_counts[name] = 1
        

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []
for value in values:
    b = value is not None and value > 30
    checks.append(b)
        
        

## 8. Highest Female Name Count ##

max_value = None
for name in name_counts:
    count = name_counts[name]
    if max_value is None or count > max_value:
        max_value = count

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for key,value in plant_types.items():
    print(key)
    print(value)

## 10. Finding the Most Common Female Names ##

top_female_names = []
for key,value in name_counts.items():
    if value == 2:
        top_female_names.append(key)

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_name_counts = {}
for item in legislators:
    if item[3] =='M' and item[7] > 1940:
        name = item[1]
        if name in male_name_counts:
            male_name_counts[name] = male_name_counts[name] + 1
        else:
            male_name_counts[name] = 1
max_value = None       
for key,value in male_name_counts.items():
    if max_value is None or value > max_value:
        max_value = value
highest_male_count = max_value
for key,value in male_name_counts.items():
    if value == highest_male_count:
        top_male_names.append(key)
    

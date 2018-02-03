## 3. Read the File Into a String ##

haha = open("dq_unisex_names.csv",'r')
names = haha.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
first_five = names_list[0:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = []
for lis in names_list:
    split_comma = lis.split(',')
    nested_list.append(split_comma)
print(nested_list[0:5])
    


## 6. Convert Numerical Values ##

print(nested_list[0:5])
numerical_list = []
for ite in nested_list:
    a = ite[0]
    b = float(ite[1])
    c = [a,b]
    numerical_list.append(c)
print(numerical_list)
    


## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater = []
for haha in numerical_list:
    if haha[1] >= 1000:
        thousand_or_greater.append(haha[0])
print(thousand_or_greater[0:9])
        
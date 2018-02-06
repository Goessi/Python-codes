## 2. Sets ##

gender = []
for item in legislators:
    gender.append(item[3])
gender = set(gender)
print(gender)

## 3. Exploring the Dataset ##

party = []
for item in legislators:
    party.append(item[6])

party = set(party)
print(party)
print(legislators)
    

## 4. Missing Values ##

for people in legislators:
    if people[3] == '':
        people[3] = 'M'
        


## 5. Parsing Birth Years ##

birth_years = []
for item in legislators:
    birth = item[2]
    parts = birth.split('-')
    birth_years.append(parts[0])
    
    

## 6. Try/except Blocks ##

try:
    ha = float('hello')
except :
    print('Error converting to float.')
# as the try part went wrong, the print will work 
# use try/except hepls us continue running the codes no matter we have error in try

## 7. Exception Instances ##

try:
    ha = int(' ')
except Exception as exc:
    print(type(exc))
    print(str(exc))

## 8. The Pass Keyword ##

converted_years = []
for ele in birth_years:
    year = ele
    try:
        year = int(year)
    except:
        pass # do nothing to the errors
    converted_years.append(year)

## 9. Convert Birth Years to Integers ##


for item in legislators:
    birthday = item[2]
    birthday = birthday.split('-')
    year = birthday[0]
    try:
        birth_year = int(year)
    except:
        birth_year = 0
    item.append(birth_year)
    

## 10. Fill in Years Without a Value ##

last_value = 1
for row in legislators:
    if row[7] == 0:
        row[7] = last_value
    else:
        last_value = row[7]

## 1. Programming And Data Science ##

print(1288)
print(639)
print(1288 + 639)

## 2. Arithmetic Operators ##

print((749 + 371 + 828 + 503 + 1379)/5)

## 3. Variables ##

albuquerque = 749
anaheim = 371
anchorage = 828
arlington = 503
atlanta = 1379
print(anaheim)

## 4. Data Types ##

atlanta_string = "Atlanta"
atlanta_float = 1379.5

## 5. The Type Function ##

atlanta_string = 'Atlanta_string'
print(type(atlanta_string)) #show the type of variables

## 6. Using A List To Store Multiple Values ##

cities = []
crime_rates = []
cities.append('Albuquerque')
cities.append('Anaheim')
cities.append('Anchorage')
cities.append('Arlington')
cities.append('Atlanta')

crime_rates.append(749)
crime_rates.append(371)
crime_rates.append(828)
crime_rates.append(503)
crime_rates.append(1379)

print(cities)
print(crime_rates)
# in one list, data type can be different,but using more space
# array.array can only contains one data type
# when it comes to MATH, import numpy
# refer from: https://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use

## 7. Creating Lists With Values ##

crime_rates = [749,371,828,503,1379]
# or use list.append(thing_you_wang_to_add)
# or create a list A = [], innitial_value = 0, A = [innitial_value for a in range(10)]

## 8. Comments ##

crime_rates = [749, 371, 828, 503, 1379]#ciuciuciuciuciuci
print(crime_rates)#hahahahahah

# to make life easier and make your collegue happy~

## 9. Accessing Elements In A List ##

cities = ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]
crime_rates = [749, 371, 828, 503, 1379]

anchorage_str = cities[2]
anchorage_cr = crime_rates[2]

# we can use the index with positive or negative integer
# A[0] is the first element of the list
# A[-1] is the last element of the list
# A[0] = A[-len(A)]
# A[-1] = A[len(A) - 1]

## 10. Retrieving The Length Of A List ##

cities = ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]
crime_rates = [749, 371, 828, 503, 1379]
# Add your code here.
a = len(cities)
b = len(crime_rates)
two_sum = a + b

## 11. Slicing Lists ##

cities = ["Albuquerque", "Anaheim", "Anchorage", "Arlington", "Atlanta"]
crime_rates = [749, 371, 828, 503, 1379]
cities_slice = cities[1:4]
a = len(crime_rates)
cr_slice = crime_rates[(a-2):(a)]

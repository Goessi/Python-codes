## 1. Introduction ##

strings = ["data science", "big data", "metadata"]
regex = "data"

## 2. Wildcards in Regular Expressions ##

strings = ["bat", "robotics", "megabyte"]
regex = "..t"
# regex matches all in strings
# special character "." to indicate that any character can be put in its place

## 3. Searching the Beginnings And Endings Of Strings ##

strings = ["better not put too much", "butter in the", "batter"]
bad_string = "We also wouldn't want it to be bitter"
regex = "^b.tter"

# "^a" will match all strings that start with "a"
# "a$" will match all strings that end with "a"

## 5. Reading and Printing the Data Set ##

import csv
file = open('askreddit_2015.csv','r')
posts_with_header = list(csv.reader(file))
posts = posts_with_header[1:]
for item in posts:
    print(item)

## 6. Counting Simple Matches in the Data Set with re() ##

# re.search(regex, string)
# we can check whether string is a match for regex
# If it is, the expression will return a match object
# If it isn't, it will return None

import re
of_reddit_count = 0
for item in posts:
    if re.search("of Reddit",item[0]) is not None:
        of_reddit_count = of_reddit_count + 1
    else:
        of_reddit_count = of_reddit_count + 0

## 7. Using Square Brackets to Match Multiple Characters ##

# useful for both upper or lower characters

import re

of_reddit_count_old = 0
for row in posts:
    if re.search("of reddit", row[0]) is not None:
        of_reddit_count_old += 1
        
of_reddit_count = 0
for item in posts:
    if re.search("of [rR]eddit",item[0]) is not None:
        of_reddit_count = of_reddit_count + 1

## 8. Escaping Special Characters ##

import re

serious_count = 0
for item in posts:
    if re.search("\[Serious\]",item[0]) is not None:
        serious_count += 1

## 9. Combining Escaped Characters and Multiple Matches ##

import re

serious_count_old = 0
for row in posts:
    if re.search("\[Serious\]", row[0]) is not None:
        serious_count_old += 1
serious_count = 0
for item in posts:
    if re.search('\[[Ss]erious]',item[0]) is not None:
        serious_count += 1

## 10. Adding More Complexity to Your Regular Expression ##

import re

serious_count_old = 0
for row in posts:
    if re.search("\[[Ss]erious\]", row[0]) is not None:
        serious_count_old += 1
serious_count = 0
for item in posts:
    if re.search("[\[(][Ss]erious[\])]",item[0]) is not None:
        serious_count += 1

## 11. Combining Multiple Regular Expressions ##

import re

serious_start_count = 0
serious_end_count = 0
serious_count_final = 0
for row in posts:
    if re.search('^[\[\(][Ss]erious[\]\)]',row[0]) is not None:
        serious_start_count += 1
    if re.search('[\[\(][Ss]erious[\]\)]$',row[0]) is not None:
        serious_end_count += 1
    if re.search('^[\[\(][Ss]erious[\]\)]|[\[\(][Ss]erious[\]\)]$',row[0]) is not None:
        serious_count_final += 1

## 12. Using Regular Expressions to Substitute Strings ##

import re
for item in posts:
    item[0] = re.sub('[\[\(][Ss]erious[\]\)]','[Serious]',item[0])


## 13. Matching Years with Regular Expressions ##

import re

year_strings = []

for year in strings:
    if re.search('[1-2][0-9][0-9][0-9]',year) is not None:
        year_strings.append(year)

## 14. Repeating Characters in Regular Expressions ##

import re
# repest [0-9] three times
# the same effect as above
year_strings = []
for year in strings:
    if re.search('[1-2][0-9]{3}',year)is not None:
        year_strings.append(year)

## 15. Challenge: Extracting all Years ##

import re
years = re.findall('[1-2][0-9]{3}',years_string)

## 4. Reading in the Data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
for i in data_files:
    a = pd.read_csv('schools/{0}'.format(i))
    key_name = i.replace('.csv','')
    data[key_name] = a

## 5. Exploring the SAT Data ##

print(data['sat_results'].head(5))

## 6. Exploring the Remaining Data ##

for k in data:
    print(data[k].head(5))

## 8. Reading in the Survey Data ##

all_survey = pd.read_csv('schools/{0}'.format('survey_all.txt'),delimiter = '\t',encoding = 'windows-1252')
d75_survey = pd.read_csv('schools/{0}'.format('survey_d75.txt'),delimiter = '\t',encoding = 'windows-1252')
survey = pd.concat([all_survey,d75_survey],axis = 0)
print(survey.head(5))

## 9. Cleaning Up the Surveys ##

#survey['DBN'] = survey['dbn']
#cols = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]
#k = survey[cols]
#data['survey'] = k

#print(k)

survey["DBN"] = survey["dbn"]

survey_fields = [
    "DBN", 
    "rr_s", 
    "rr_t", 
    "rr_p", 
    "N_s", 
    "N_t", 
    "N_p", 
    "saf_p_11", 
    "com_p_11", 
    "eng_p_11", 
    "aca_p_11", 
    "saf_t_11", 
    "com_t_11", 
    "eng_t_11", 
    "aca_t_11", 
    "saf_s_11", 
    "com_s_11", 
    "eng_s_11", 
    "aca_s_11", 
    "saf_tot_11", 
    "com_tot_11", 
    "eng_tot_11", 
    "aca_tot_11",
]
survey = survey.loc[:,survey_fields]
data["survey"] = survey

print(survey.head())

## 11. Inserting DBN Fields ##

data['hs_directory']['DBN'] = data['hs_directory']['dbn']

def pad_csd(num):
    if len(str(num)) < 2:
        num = str(num).zfill(2)
        return num
    else:
        return str(num)
data['class_size']['padded_csd'] = data['class_size']['CSD'].apply(pad_csd)
data['class_size']['DBN'] = data['class_size']['padded_csd'] + data['class_size']['SCHOOL CODE']

print(data['class_size']['DBN'].head())

## 12. Combining the SAT Scores ##

data['sat_results']['SAT Math Avg. Score'] = pd.to_numeric(data['sat_results']['SAT Math Avg. Score'],errors = 'coerce')
data['sat_results']['SAT Critical Reading Avg. Score'] = pd.to_numeric(data['sat_results']['SAT Critical Reading Avg. Score'], errors = 'coerce')
data['sat_results']['SAT Writing Avg. Score']=pd.to_numeric(data['sat_results']['SAT Writing Avg. Score'],errors = 'coerce')

data['sat_results']['sat_score'] = data['sat_results']['SAT Math Avg. Score'] + data['sat_results']['SAT Critical Reading Avg. Score'] + data['sat_results']['SAT Writing Avg. Score']

print(data['sat_results']['sat_score'].head())

## 13. Parsing Geographic Coordinates for Schools ##

import re
def find_lat(aStr):
    a = re.findall('\(.+\)',aStr)
    lat = a[0].split(',')[0].replace('(','')
    return lat
data['hs_directory']['lat'] = data['hs_directory']['Location 1'].apply(find_lat)

print(data['hs_directory'].head())

## 14. Extracting the Longitude ##

import re
def find_lon(aStr):
    a = re.findall('\(.+\)',aStr)
    lon = a[0].split(',')[1].replace(')','')
    return lon
data['hs_directory']['lon'] = data['hs_directory']['Location 1'].apply(find_lon)
data['hs_directory']['lat'] = pd.to_numeric(data['hs_directory']['lat'],errors = 'coerce')
data['hs_directory']['lon'] = pd.to_numeric(data['hs_directory']['lon'],errors = 'coerce')

print(data['hs_directory'].head())

## 2. Overview of the Data ##

import pandas as pd
submissions = pd.read_csv("sel_hn_stories.csv")
submissions.columns = ["submission_time", "upvotes", "url", "headline"]
submissions = submissions.dropna()

## 3. Tokenizing the Headlines ##

tokenized_headlines = []
for row in submissions.iloc[:,3]:
    row = row.split(' ')
    tokenized_headlines.append(row)

## 4. Preprocessing Tokens to Increase Accuracy ##

punctuation = [",", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
clean_tokenized = []
for item in tokenized_headlines:
    words = []
    for word in item:
        word = word.lower()
        for pun in punctuation:
            word = word.replace(pun,'')
        words.append(word)
    clean_tokenized.append(words)
        

## 5. Assembling a Matrix of Unique Words ##

import numpy as np
unique_tokens = []
single_tokens = []
for each_list in clean_tokenized:
    for token in each_list:
        if token in single_tokens:
            single_tokens.remove(token)
            if token not in unique_tokens:
                unique_tokens.append(token)
        else:
            single_tokens.append(token)
counts = pd.DataFrame(0, index=np.arange(len(clean_tokenized)), columns=unique_tokens)
print(unique_tokens)

## 6. Counting Token Occurrences ##

for index,tokens in enumerate(clean_tokenized):
    for token in tokens:
        if token in unique_tokens:
            counts[token][index] += 1

## 7. Removing Columns to Increase Accuracy ##

word_counts = counts.sum(axis=0)
counts = counts.loc[:,(word_counts>=5)&(word_counts<=100)]

## 9. Making Predictions With fit() ##

from sklearn.linear_model import LinearRegression

clf = LinearRegression()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

## 10. Calculating Prediction Error ##

mse = (((y_test - predictions)**2).sum())/len(predictions)

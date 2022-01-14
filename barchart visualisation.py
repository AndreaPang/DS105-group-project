import pandas as pd
import numpy as np
#load inthe NTLK stopwords to remove articles, preposition and other words that are not actionable
from nltk.corpus import stopwords
# This allows to create individual objects from a bog of words
from nltk.tokenize import word_tokenize
# Lemmatizer helps to reduce words to the base form
from nltk.stem import WordNetLemmatizer
# Ngrams allows to group words in common pairs or trigrams..etc
from nltk import ngrams
# We can use counter to count the objects
from collections import Counter
# This is our visual library
import seaborn as sns
import matplotlib.pyplot as plt

word_freq=pd.read_csv('/Users/Andrea/Desktop/DS105/data1/result1.csv', usecols=['word','frequency'])
word_pairs=pd.read_csv('/Users/Andrea/Desktop/DS105/data1/result2.csv', usecols=['pairs','frequency'])


data2=word_freq
data3=word_pairs
#print(type(data2))
# create subplot of the different data frames
fig, axes = plt.subplots(2,1,figsize=(8,20))
sns.barplot(ax=axes[0],x='frequency',y='word',data=data2.head(20))
sns.barplot(ax=axes[1],x='frequency',y='pairs',data=data3.head(20))
#sns.barplot(ax=axes[2],x='frequency',y='trigrams',data=data4.head(10))
plt.show()
#	


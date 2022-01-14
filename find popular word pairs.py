# loading in all the essentials for data manipulation
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




text_1=pd.read_csv('/Users/Andrea/Desktop/DS105/data/new_mid-pandemic1.csv')
text_1.columns = ['text','Unnamed: 1']
sentences = list(text_1.text)
#sentences=sentences

def word_frequency(sentence):
	sentence =" ".join(sentence)
	new_tokens = word_tokenize(sentence)
	new_tokens = [t.lower() for t in new_tokens]
	new_tokens =[t for t in new_tokens if t not in stopwords.words('english')]
	new_tokens = [t for t in new_tokens if t.isalpha()]
	lemmatizer = WordNetLemmatizer()
	new_tokens =[lemmatizer.lemmatize(t) for t in new_tokens]
	counted = Counter(new_tokens)
	counted_2= Counter(ngrams(new_tokens,2))
	counted_3= Counter(ngrams(new_tokens,3))
	word_freq = pd.DataFrame(counted.items(),columns=['word','frequency']).sort_values(by='frequency',ascending=False)
	word_pairs =pd.DataFrame(counted_2.items(),columns=['pairs','frequency']).sort_values(by='frequency',ascending=False)
	trigrams =pd.DataFrame(counted_3.items(),columns=['trigrams','frequency']).sort_values(by='frequency',ascending=False)
#	return word_freq,word_pairs,trigrams
	word_freq.to_csv('/Users/Andrea/Desktop/DS105/data1/result3.csv')
	word_pairs.to_csv('/Users/Andrea/Desktop/DS105/data1/result4.csv')

word_frequency(sentences)


text_2=pd.read_csv('/Users/Andrea/Desktop/DS105/data/new_late-pandemic1.csv')
text_2.columns = ['text','Unnamed: 1']
sentences2 = list(text_2.text)
#sentences=sentences

def word_frequency_1(sentence):
	sentence =" ".join(sentence)
	new_tokens = word_tokenize(sentence)
	new_tokens = [t.lower() for t in new_tokens]
	new_tokens =[t for t in new_tokens if t not in stopwords.words('english')]
	new_tokens = [t for t in new_tokens if t.isalpha()]
	lemmatizer = WordNetLemmatizer()
	new_tokens =[lemmatizer.lemmatize(t) for t in new_tokens]
	counted = Counter(new_tokens)
	counted_2= Counter(ngrams(new_tokens,2))
	counted_3= Counter(ngrams(new_tokens,3))
	word_freq = pd.DataFrame(counted.items(),columns=['word','frequency']).sort_values(by='frequency',ascending=False)
	word_pairs =pd.DataFrame(counted_2.items(),columns=['pairs','frequency']).sort_values(by='frequency',ascending=False)
	trigrams =pd.DataFrame(counted_3.items(),columns=['trigrams','frequency']).sort_values(by='frequency',ascending=False)
#	return word_freq,word_pairs,trigrams
	word_freq.to_csv('/Users/Andrea/Desktop/DS105/data1/result5.csv')
	word_pairs.to_csv('/Users/Andrea/Desktop/DS105/data1/result6.csv')

word_frequency_1(sentences2)
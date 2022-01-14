import pandas as pd
text_1=pd.read_csv('/Users/Andrea/Desktop/DS105/data/new_pre-pandemic1.csv')
text_1.columns = ['text','Unnamed: 1']
#print(text_1)


sentences = list(text_1.text)
#print(sentences[64430])

import nltk

#Stopwords
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

def lowercase(word):
	return word.lower()

def splt(sent):
    return sent.split()

sentences = list(map(splt, sentences))
print(sentences[0:10])

vocabulary = set(sentences[0])
clean_text = []
for word in vocabulary:
	if lowercase(word) not in stop:
		clean_text.append(word)
#print(clean_text[0:10])
#
#import json
#
def processSentences(sent):
	return list(map(lowercase, sent))
sentences=list(map(processSentences,sentences))
#
#
affin = open('/Users/Andrea/Desktop/DS105/data/AFINN_english.txt')
sentimentScores = {}
#
for line in affin:
	term, score = line.split("\t")
	sentimentScores[term] = float(score)
#
##Proceed with sentiment analysis
TwittsSentiment = []
#
for sent in sentences:
    score = 0
    for word in sent:
        try:
            score += sentimentScores[word]
        except:
            pass
    TwittsSentiment.append(score)
#
##print(TwittsSentiment) 
#
df = pd.DataFrame({'scores_pre': TwittsSentiment})
df.to_csv('/Users/Andrea/Desktop/DS105/data/TwittsSentiment_pre-pandemic.csv')

# with open('/Users/Andrea/Desktop/DS105/data/TwittsSentiment_pre-pandemic.csv','w',encoding='UTF8') as new_file:
# 	fieldnames=['score']	
# 	csv_writer=csv.writer(new_file)
#    csv_writer.writerow=(TwittsSentiment)
		
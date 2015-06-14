# -*- coding: utf-8 -*-
"""
@author: 'deepthi'
"""
import string 
import re
import nltk
from nltk.tokenize import word_tokenize 
from sklearn.externals import joblib

def read_data():
    with open("/Users/deepthi/Downloads/as.txt", 'r') as fileinput:
        lines= [filter(lambda x: x in string.printable, (re.sub(r"(?:\@|https?\://)\S+", "", line)).lower().translate(None, string.punctuation)) for line in fileinput]
    print lines[0]
    tokenize = [word_tokenize(text)  for text in lines]
    return lines,tokenize
    

def similar(data):
    for tokens in data:
        verb = [toks[0] for toks in nltk.pos_tag(tokens) if toks[1] in ['VB','JJ']]
    print verb
    
def create_model(data):
    unigrams=[]
    for words in data:
        for tokens in word_tokenize(words):
            unigrams.append(tokens)
    cfreq_data_bigram = nltk.ConditionalFreqDist(nltk.bigrams((unigrams)))
    return cfreq_data_bigram

def main_code():
    data,tokenized_data = read_data()
    joblib.dump(data,"Data_Model.pkl")
    model1 = create_model(data)
    joblib.dump(model1,"Modeldump_Bigram.pkl")
  
if __name__ == "__main__":
    main_code()
  

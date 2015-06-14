# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 17:03:29 2015
@author: 'deepthi'
"""
from sklearn.externals import joblib
import string
from nltk.tokenize import word_tokenize 
import re


def read_data(data1):
    flag ="N"
    lines= filter(lambda x: x in string.printable, (re.sub(r"(?:\@|https?\://)\S+", "", data1)).lower().translate(None, string.punctuation))
    tokenized = word_tokenize(lines)
    data = joblib.load("Data_Model.pkl")
    for tokens in data:
        if str(lines).rstrip() == str(tokens).rstrip():
            flag ="Y"
    if flag =="N":
        model = joblib.load("Modeldump.pkl")
        output = model[tokenized.pop()] 
    else:
        output = data1
    return output,flag

def main_call():
    outer1=""
    outer2=""
    enter_input = str(raw_input(("Please enter the text: ")))
    output,flag = read_data(enter_input)
    if flag == "N":
        outer1=max(output, key=output.get)
        new_enter_input = str(enter_input) +" "+ str(outer1)
        output1,flag1 = read_data(new_enter_input)
        if flag1 == "N":
           outer2=max(output1, key=output1.get)
           print str(outer1) +" "+ str(outer2)
        else:
            print output1
    else:
        print output

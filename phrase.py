import numpy as np
import pandas as pd
import json
from collections import defaultdict
import nltk
from nltk.translate.phrase_based import phrase_extraction
from model1 import *

with open('data1.json') as f:
    data = json.load(f)
basicList=final_list

#with open('alignment.txt', 'r') as f:
#    basicList = txt.load(f)
#basicList=basicList[1:-1]
#print(basic)

sentence_pair=[]
for x in data[:]:
    sentence_pair.append([x['en'],x['fr']])

count=defaultdict(lambda:defaultdict(int))
list=[]
dict=[]
temp=0
al=[]
for x in sentence_pair:
    en=x[0]
    fr=x[1]
    al=basicList[temp]
#    print(al)
    temp+=1
#    al=[(0,0), (1,1), (2,2), (3,3), (4,4)]
    #Using nltk phrase_extraction to automatically generate phrases as tuples
    phrases= phrase_extraction(en,fr,al)
    for x in phrases:
        dict.append(x)
#        print("m")

for i in dict:
    fr=i[3]
    en=i[2]
    count[en][fr]+=1

#Creating a final dictionary sorted according to value
sortedDict={}
for en in count:
#    length= len(count[en])
    length=0
    for fr in count[en]:
        length+= count[en][fr]
    for fr in count[en]:
        num=count[en][fr]
        
        #probability of each phrase
        prob=float(num)/float(length)
        sortedDict[fr+','+en]=prob
        list.append(fr+','+en+': '+str(prob))

print(final_list)
s=sorted(sortedDict.items(),key=lambda x:x[1],reverse=True)
for key,val in s:
#    if(val>1.0):
#        continue
    print(key+': '+str(val))
#print(list)

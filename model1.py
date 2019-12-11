import numpy as np
import pandas as pd
import json

foreign_file = open('Foreign1.txt')
english_file = open('English1.txt')

#foreign_file = open('Foreign2.txt')
#english_file = open('English2.txt')

foreign_list = []
english_list = []

for f in foreign_file:
    foreign_list.append(f)
for e in english_file:
    english_list.append(e)

list_english_sent = []

list_foreign_sent = []
for i in range(len(english_list)):
    list_english_sent.append(english_list[i].split())
    list_foreign_sent.append(foreign_list[i].split())


# sentence_pair=[[['dog','barked'],['hund','bjeffet']],[['dog','bit','dog'],['hund','bet','hund']]]
sentence_pair = []

for i in range(len(list_english_sent)):
    l = []
    l.append(list_english_sent[i])
    l.append(list_foreign_sent[i])
    sentence_pair.append(l)

english_word=[]
foreign_word=[]

for sp in sentence_pair:
    for word in sp[0]:
        english_word.append(word)
    for word in sp[1]:
        foreign_word.append(word)

print(english_word)
print(foreign_word)

english_word=list(set(english_word))
foreign_word=list(set(foreign_word))

english_word.sort()
foreign_word.sort()

print(len(english_word))
print(len(foreign_word))


# In[21]:


t={}
count={}
total={}
s_total={}
x=len(foreign_word)
for e in english_word:
    for f in foreign_word:
        tup=(e,f)
        t[tup]=1.0/x

print((t))


# In[22]:


for i in range(1000):
    for x in t:
        count[x]=0.0
    for x in foreign_word:
        total[x]=0.0
    for sp in sentence_pair:
        for e in sp[0]:
            s_total[e]=0.0
            for f in sp[1]:
                s_total[e]+=t[(e,f)]
        for e in sp[0]:
            for f in sp[1]:
                count[(e,f)]+=t[(e,f)]/s_total[e]
                total[f]+=t[(e,f)]/s_total[e]
    for f in foreign_word:
        for e in english_word:
            t[(e,f)]=count[(e,f)]/total[f]

#print(t)
# for s in t:
#     print(s[0]+" "+s[1])
print(len(t))
          
for e in english_word:
    maxs=0.0
    strings=""
    for s in foreign_word:
        if(t[(e,s)]>maxs):
            maxs=t[(e,s)]
            strings=s
            #print("*")
    print(e+" "+strings+" "+str(maxs))
    
    


# In[24]:


sentcount=1;
final_list=[]
for sp in sentence_pair:
    list_of_tuples=[]
    count1=0
    print("******************")
    print(sentcount)
    sentcount+=1
    for f in sp[1]:
        count1+=1
        maxs=0.0
        count2=0
        fin=0
        for e in sp[0]:
            count2+=1
            if(t[(e,f)]>maxs):
                fin=count2
                maxs=t[(e,f)]
        tup=(count1-1,fin-1)
        list_of_tuples.append(tup)
        print(str(count1)+" "+str(fin))
        string_list=str(list_of_tuples)

    final_list.append(list_of_tuples)

#final_string=str(final_list)
print(final_list)
#with open('alignment.json', 'w') as fp:
#    json.dump(final_string, fp,ensure_ascii=False)


#
#  IBM Model 1 Lexical translation model that ignores word order.
#
# In IBM Model 1, word order is ignored for simplicity. As long as the
# word alignments are equivalent, it doesn't matter where the word occurs
# in the source or target sentence. so the alignments
# are equally likely.
#
#
# Source: du jambon je mange
# Target: eat i some ham
# Alignment: (0,3) (1,2) (2,0) (3,1)
#
#
# IBM Model 2 Lexical translation model that considers word order.
#
# IBM Model 2 improves on Model 1 by accounting for word order.
# An alignment probability is introduced, a(i | j,l,m), which predicts
# a source word position, given its aligned target word's position.
#


from nltk.translate import IBMModel1, AlignedSent , Alignment , IBMModel2
x = []
y = []
with open('Foreign1.txt', 'r') as f:
    x = f.readlines()
with open('English1.txt', 'r') as f:
    y = f.readlines()

#with open('Foreign2.txt', 'r') as f:
#    x = f.readlines()
#with open('English2.txt', 'r') as f:
#    y = f.readlines()

list_eng = []
list_fore = []
for i in range(len(x)):
       list_eng.append(x[i].split())
       list_fore.append(y[i].split())
data = []
bitext = []
for i in range(len(list_eng)):
      l = []
      l.append(list_eng[i])
      l.append(list_fore[i])
      data.append(l)
      bitext.append(AlignedSent(list_eng[i],list_fore[i]))


ibm1 = IBMModel1(bitext, 5)
ibm2 = IBMModel2(bitext, 5)
corpus = []
for i in data:
     for j in i:
         for k in j:
          if not k in corpus:
            corpus.append(k)
print(bitext)

print("first word  "  +  "second word  " + "        ibmmodel1  " + "        ibmmodel2 ")
for i in corpus :
    for j in corpus :
      if((i!=j) and (ibm1.translation_table[i][j] > 0.000005 or ibm2.translation_table[i][j] >  0.000005 ) ):

         print(i + "         " +   j + "       " + str( ibm1.translation_table[i][j]) + "            "+ str(ibm2.translation_table[i][j]))
#for i in data :
#
#    print(ibm2.alignment_table[1][1][2][2])

import pandas as pd
import operator
import matplotlib as plt

N=10
documents=[]
for i in range(10):
    searchfile = open("Documents\\freq-t"+str(i+1)+".txt", "r")
    doci=[]
    for line in searchfile:
        line=line.split(":")
        doci.append(line[0])
    documents.append(doci)
    searchfile.close()
#print(documents)

Nw=dict()
docs=[]
for i in range(10):
    docs=docs+documents[i]

#print(docs)
docs=list(set(docs))

def compute(nw):
    return ((N-nw+0.5)/(nw+0.5))

table=dict()
for x in docs:
    nw=0
    list1=[]
    for i in documents:
        if x in i:
            nw+=1
    list1.append(nw) # Number of Occurances of the word in each document
    calc=compute(nw)
    list1.append(calc) # Probabilistic value of every word in each document
    table[x]=list1
#print(table)

query=input("Enter query :").split(" ")

pdl=dict()

for i in range(N):
    pdi=1
    for x in query:
        if x in documents[i]:
            pdi=pdi*table[x][1]
        else:
            pdi=0
    pdl[i+1]=pdi

sort = pdl

sort= {k: "{0:.5f}".format(j) for k, j in sorted(sort.items(), key=lambda item: item[1], reverse=True)}   #first parameter value is items() // The "key" parameter provides a function that says how to sort them. We have named the param as lambda expression

print(pd.DataFrame(sort.items(),columns=['Fno','Rel']))


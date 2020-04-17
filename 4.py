import math

def ranking(docs,rank):
    for i in range(len(rank)-1,-1,-1):
        for j in range(len(docs)):
            if rank[i]==docs[j]:
                print('Document '+str(j+1)+" "+str(rank[i]))

def inverse_doc_freq(idf,contents):
    k=-1
    for line in contents:
        k+=1
        l=list(line.split())
        c=0
        if l[2]!="0":
            c+=1
        if l[3]!="0":
            c+=1
        if l[4]!="0":
            c+=1
        if l[5]!="0":
            c+=1
        if l[6]!="0":
            c+=1
        if l[7]!="0":
            c+=1
        if l[8]!="0":
            c+=1
        if l[9]!="0":
            c+=1
        if l[10]!="0":
            c+=1
        if l[11]!="0":
            c+=1
        idf[k]=math.log2(10/int(c))

def weight_vector(tf,idf,count):
    weight=[]
    for i in range(count):
        weight.append([])
        for j in range(10):
            weight[i].append(tf[i][j]*idf[i])
    
    
    return weight

def similarity(doc,query):
    prod=0
    mag_doc=0.0
    mag_query=0.0
    for i in range(len(doc)):
        mag_doc+=doc[i]*doc[i]
        mag_query+=query[i]*query[i]
        prod+=doc[i]*query[i]
    mag_doc=math.sqrt(mag_doc)
    mag_query=math.sqrt(mag_query)
    #print(prod,mag_doc,mag_query)
    return prod/(mag_doc*mag_query)

###MAIN####

f=open("Inverted-Index\\target.txt","r")
contents=f.readlines()
count=0
for line in contents:
    count+=1
#tf=[[0]*10]*count
tf=[]
idf=[0]*count
i=-1
for line in contents:
    i+=1
    l=list(line.split())
    tf.append([])
    for j in range(10):
        tf[i].append(float(l[j+2])) # For every word - 1 array wich contains the no of occurances of that word in every document
#print(tf)
    
inverse_doc_freq(idf,contents) 
doc_weight=weight_vector(tf,idf,count)  
#print(doc_weight) 
rank=[-1]*10
q=input('Enter a query\n')
q_list=[x for x in q.split()]
q_set=set([x for x in q.split()])
freq={}
query=[0]*count
i=-1
for j in q_set:
    freq[j]=0
for j in q_list:
    freq[j]+=1
for line in contents:
    i+=1
    l=list(line.split())
    for j in q_set:
        if l[0]==j:
            query[i]=(freq[j]/len(q_set))*idf[i]
d=[]
for i in range(10):
    d.append([])
    for j in range(count):
        d[i].append(doc_weight[j][i])
    rank[i]=similarity(d[i],query)

docs = rank[:]
rank=sorted(rank)
print(rank)
print('Rank')
ranking(docs,rank)
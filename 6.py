import matplotlib.pyplot as plt

# (PART A) Calculate recall and precision values for all relevant documents and draw precision VS Recall Curve. Also calculate R-precision.

rQ = ['d3','d5','d9','d25','d39','d44','d56','d71','d89','d123']
aQ = ['d123','d84','d56','d6','d8','d9','d511','d129','d187','d25','d38','d48','d250','d113','d3']
aQ1 = ['d12','d39','d13','d123','d8','d9','d19','d89','d87','d25','d70','d71','d29','d44','d3']

p = {}
r = {}
x = [0] # x axis values  
y = [100] # corresponding y axis values 
relevant = 0
for i in range(len(aQ)):
    doc = aQ[i]
    if (doc in rQ):
        relevant += 1
        p[doc] = (relevant / (i + 1)) * 100
        r[doc] = (relevant / len(rQ)) * 100
        x.append(r[doc])
        y.append(p[doc])

print("\nPrecision of relevant docs (1): \n", p)
print("Recall of relevant docs (1): \n", r)

x.extend([60,70,80,90,100])
y.extend([0,0,0,0,0])
   
plt.plot(x, y, color='red', marker='o', markerfacecolor='red', markersize=6) # plotting the points  
plt.xlabel('Recall') # naming the x axis 
plt.ylabel('Precision') # naming the y axis  
plt.title('Precision VS Recall') # giving a title to my graph
plt.show() # function to show the plot 

count=0
for i in range(len(rQ)):
    if aQ[i] in rQ:
       count+=1
print("\nR Precision (1): " + str(count*100/(len(rQ)))) # Precision at the index R

# (PART B) Compare performance of two IR algorithms for the same query q.

p1 = {}
r1 = {}
x2 = [0] 
y2 = [100] 
relevant = 0
for i in range(len(aQ1)):
    doc = aQ1[i]
    if (doc in rQ):
        relevant += 1
        p1[doc] = (relevant / (i + 1)) * 100
        r1[doc] = (relevant / len(rQ)) * 100
        x2.append(r1[doc])
        y2.append(p1[doc])

print("\nPrecision of relevant docs (2): \n", p1)
print("Recall of relevant docs (2): \n", r1)

x2.extend([90,100])
y2.extend([0,0])

plt.plot(x, y, label = "Algorithm 1", color='red', marker='o', markerfacecolor='red', markersize=6) 
plt.plot(x2, y2, label = "Algorithm 2", color='blue', marker='o', markerfacecolor='blue', markersize=6) 
plt.xlabel('Recall') 
plt.ylabel('Precision') 
plt.title('Performance comaprison of two IR algorithms for the same query')  
plt.legend() # show a legend on the plot
plt.show() 

count1=0
for i in range(len(rQ)):
    if aQ1[i] in rQ:
       count1+=1
print("\nR Precision (2): " + str(count1*100/(len(rQ)))) # Precision at the index R
print("")
if count1 > count:
    print("Since R-Precision is higher Algorithm aQ1 is better\n")
else:
    print("Since R-Precision is higher Algorithm aQ2 is better\n")

def harmonic_mean(a,b):
    return 2/((100/a)+(100/b))
hm={}
for doc in p:
    hm[doc]=harmonic_mean(p[doc],r[doc])

print("Harmonic Mean :")
print(hm)

b=[0.1,1,2]
def Emeasure(r,p,b):
    Em=[]
    for i in b:
        x = i*i
        if i<1:
            Em.append(1-((1+x)/(((x*100)/r)+(100/p))))
        if i==1:
            Em.append(1-harmonic_mean(r,p))
        if i>1:
            Em.append(1-((1+x)/(((x*100)/r)+(100/p))))
    return Em
Em={}
for doc in p:
    Em[doc]=Emeasure(r[doc],p[doc],b)

print("\nE measure for [0.5, 1, 2]: ")
print(Em)

# Inverted Index

from _collections import defaultdict

def util_helper(contents,d,pos):
    for word in contents.split():
        #if word not in d.keys():
            d[word].append(pos)

def document_frequency(doc_freq,d,pos):
    for word in d.keys():
        count=0
        #print(len(d[word]))
        for i in range(len(d[word])):
            if d[word][i]==pos:
                count+=1
        doc_freq[word]=count

def index():
    f1=open("Inverted-Index\doc1.txt","r")
    f2 = open("Inverted-Index\doc2.txt", "r")
    f3 = open("Inverted-Index\doc3.txt", "r")
    f4 = open("Inverted-Index\doc4.txt", "r")
    f5= open("Inverted-Index\doc5.txt", "r")
    f6= open("Inverted-Index\doc6.txt", "r")
    f7= open("Inverted-Index\doc7.txt", "r")
    f8= open("Inverted-Index\doc8.txt", "r")
    f9= open("Inverted-Index\doc9.txt", "r")
    f10= open("Inverted-Index\doc10.txt", "r")
    d=defaultdict(list)
    freq={}
    f_list=[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]
    for i in range(10):
        contents=f_list[i].read()
        util_helper(contents,d,i+1)
    document_list=[]
    for i in range(10):
        doc_freq={}
        document_frequency(doc_freq,d,i+1)
        document_list.append(doc_freq)
    for word in d.keys():
        freq[word]=len(d[word])
        d[word]=set(d[word])
    #print(freq)
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    f9.close()
    f10.close()
    f2=open("Inverted-Index\display.txt","w")
    f1=open("Inverted-Index\\target.txt","w")
    f2.write("  Word\t\t\t\tDocument List\t\t\tTotal_Frequency\t\tDoc1_Freq\t\tDoc2_Freq\t\tDoc3_Freq\t\tDoc4_Freq\t\tDoc5_Freq\t\tDoc6_Freq\t\tDoc7_Freq\t\tDoc8_Freq\t\tDoc9_Freq\t\tDoc10_Freq\n\n")
    for word in sorted(d.keys()):
        f1.write(word.rjust(8)+'\t\t\t'+str(freq[word]).rjust(8)+'\t\t'+str(document_list[0][word]).rjust(8)+'\t\t'+str(document_list[1][word]).rjust(8)+'\t\t'+str(document_list[2][word]).rjust(8)+'\t\t'+str(document_list[3][word]).rjust(8)+'\t\t'+str(document_list[4][word]).rjust(8)+'\t\t'+str(document_list[5][word]).rjust(8)+'\t\t'+str(document_list[6][word]).rjust(8)+'\t\t'+str(document_list[7][word]).rjust(8)+'\t\t'+str(document_list[8][word]).rjust(8)+'\t\t'+str(document_list[9][word]).rjust(8))
        f1.write("\n")
        f2.write(
            word.rjust(8) + '\t\t\t' + str(d[word]).rjust(8) + "\t\t\t\t" + str(freq[word]).rjust(8) + '\t\t' + str(
                document_list[0][word]).rjust(8) + '\t\t' + str(document_list[1][word]).rjust(8) + '\t\t' + str(
                document_list[2][word]).rjust(8) + '\t\t' + str(document_list[3][word]).rjust(8)+ '\t\t' + str(document_list[4][word]).rjust(8)+ '\t\t' + str(document_list[5][word]).rjust(8)+ '\t\t' + str(document_list[6][word]).rjust(8)+ '\t\t' + str(document_list[7][word]).rjust(8)+ '\t\t' + str(document_list[8][word]).rjust(8)+ '\t\t' + str(document_list[9][word]).rjust(8))
        f2.write("\n")

    f1.close()
    return d
def search(text,d):
    f1=open("Inverted-Index\display.txt","r")
    contents=f1.readlines()
    for line in contents:
        l=list(line.split())
        word=''.join(l[:1])
        if word==text:
            print("doc:"+str(d[word])+" frequency:"+l[2+(len(d[word])-1)])

text=input("Enter the text to be searched\n")
d=index()
search(text,d)
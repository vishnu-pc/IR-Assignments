# Document Pre-Processing

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
import os
def lexical_analysis(f):
    contents = f.read()
    pattern='[0-9]'
    newf = open("Preprocessing_text\lex.txt", "w")
    for word in contents.split():
        words=''
        word=re.sub(pattern,'', word)+" "
        for i in word:
            if i not in string.punctuation:
                words+=i
            else:
                words+=' '
        words=words.lower()
        newf.write(words)
    print("Size of the file in bytes (After) lexical analysis: "+str(os.stat("Preprocessing_text\lex.txt").st_size))
    newf.close()
def stop_words():
    newf=open("Preprocessing_text\lex.txt", "r")
    newf1=open("Preprocessing_text\stop.txt","w")
    contents = newf.read()
    stop=list(stopwords.words('english'))
    for word in contents.split():
        if word not in stop:
            newf1.write(word+' ')
    newf.close()
    newf1.close()
    print("Size of the file in bytes (After) removing stopwords: " + str(os.path.getsize("Preprocessing_text\stop.txt")))

def stemming():
    newf1=open("Preprocessing_text\stop.txt","r")
    newf2=open("Preprocessing_text\stem.txt","w")
    ps=PorterStemmer()
    contents=newf1.read()
    for word in contents.split():
        newf2.write(ps.stem(word)+" ")
    newf1.close()
    newf2.close()
    print("Size of the file in bytes (After) stemming: " + str(os.stat("Preprocessing_text\stem.txt").st_size))

f = open("Preprocessing_text\Text3.txt", "r", encoding="utf-8", errors='ignore')
print("Size of the file in bytes (Before): "+str(os.stat("Preprocessing_text\Text3.txt").st_size))
lexical_analysis(f)
#nltk.download('stopwords')
stop_words()
stemming()
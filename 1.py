# KMP 

def failure(p):
    lps=[0]*len(p)
    j=0
    i=1
    while i<len(p):
        if p[i]==p[j]:
            j=j+1
            lps[i]=j
            i+=1
        else:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
    return lps            
            
def matching(s,p):
    (i,j)=(0,0)
    lps=failure(p)
    while i<len(s) and j<len(p):
        if s[i]==p[j]:
            i+=1
            j+=1
        if j==len(p):
            print('Pattern found:'+str(i-j))
        elif i<len(s) and s[i]!=p[j]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1

# Rabin

d=256
def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i,j,p,t = 0,0,0,0
    h = 1
 
    for i in range(M-1):
        h = (h*d)%q
 
    for i in range(M):
        p = (d*p + ord(pat[i]))%q
        t = (d*t + ord(txt[i]))%q
 
    for i in range(N-M+1):
        if p==t:
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
 
            j+=1
            if j==M:
                print("Pattern found at index " + str(i))
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q
            if t < 0:
                t = t+q
 

# Run

def run():
    ip = "4"
    while(ip != "3"):
        ip = input('Which Pattern-Matching algorithm would you like to use:\n1.KMP\n2.Rabin\n3.Enter any key to Exit\n')
        if ip == "1": 
            s=input('Enter a string\n')
            p=input('Enter a pattern\n')
            matching(s,p)
        elif ip == "2":
            txt = input('Enter a string\n')
            pat = input('Enter a pattern\n')
            q = 101
            search(pat,txt,q)
        else:
            ip = "3"

run()
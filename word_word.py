def A(w1,w2):
    ww1=list(w1)
    ww2=list(w2)
    a=[]
    ass=len(ww2) 
    for l1 in range( len(ww1)):
        ass-=1
        if ass>=0: 
           a.append(ord (ww1[l1]) - ord (ww2[l1]))
        
    c=len(ww1)-len(ww2)    
    a.append(c)
    b=sum(a)
    print (b)
    print(a)
w1=input('enter a word1  :')    
w2=input('enter a word2  :')    
er=A(w1,w2)  
 

   
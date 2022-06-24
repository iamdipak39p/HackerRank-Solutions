scores=[4,21,36,2,10,28,35,5,24,42]
max=scores[0]
min=scores[0]
c1=0
c2=0
recordBreakCount=[]
for i in range(0,len(scores)):
    if scores[i]>max:
        max=scores[i]
        c1=c1+1

    if scores[i]<min:
        min=scores[i]
        c2+=1

recordBreakCount.extend([c1,c2])

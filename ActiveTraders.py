customers=["z","aaa","bbb","bbb","bbb","bbb","bbb","bbb","cc","cc","cc","cc","cc","cc","cc","cc","cc","cc","cc","cc","cc","cc","cc"]
print(sorted(customers))
cust=[]
per=[]
Activetraders=[]
i=0
for each in customers:
    if each not in cust:
        cust.append(each)


for each in cust:
    per.append(customers.count(each)/len(customers)*100)

for i in range(0,len(cust)):
    if per[i]>5:
        Activetraders.append(cust[i])
print(Activetraders)

h=str(input())
listh=list(h)
listn=[]
for i in range(0,len(listh)):
    if(i%2==0):
        listn.insert(i+1,listh[i])
    elif(i%2==1):
        listn.insert(i-1,listh[i])
print(''.join(listn))

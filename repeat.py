l=int(input())
h=list(map(int,input().split()))[:l]
m=[]
for i in range(len(h)):
    k=i+1
    for j in range(k,len(h)) :
        
        if(h[i]==h[j] and s[i] not in m):
            m.append(h[i])
m.sort()
if(m):
    for i in m:
        print(i,end=" ")
else:
    print("unique")

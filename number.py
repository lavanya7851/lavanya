l,n=map(int,input().split())
for i in range (l+1,n):
if m>1:
for i in range(2,m):
if(m%i)==0:
break
else:
print(m,end=' ')

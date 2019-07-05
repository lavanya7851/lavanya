from itertools import combinations
(l, x) =input().split()
x=int(x)
arr=[]
comb=combinations(l,len(l)-x)
comb=list(comb)
#print(comb)
for i in (comb):
    arr.append("".join(i))
#print(arr)
print(min(arr))
#for i in list(comb):
#    arr.append()

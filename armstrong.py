x,o=map(int,input().split())
for i in range(x+1,o):
  sum=0
  d=i
  while d>0:
    s=d%10
    sum=sum+s**3
    d=d//10
    if (sum==i):
      print(i,end=" ")

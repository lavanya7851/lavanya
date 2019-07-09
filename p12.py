ss=list(map(int,input().split()))
a=list(map(int,input().split()))
for i in range(0,ss[1]):
  a=[a[-1]] + a[:-1]
print(*a,end=' ')

nn,k=map(int,input().split())
for i in range(max(nn,k),100000):
    if(i%nn==0 and i%k==0):
        print(i)
        break

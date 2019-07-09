nn1,nn2=map(int,input().split())
for i in range(1,100000):
   if(i%nn1==0 and i%nn2==0):
      print(i)
      break

ll = int(input())
b=[]
for i in range(0,ll):
 input=input()
 b.append(input)
mn=[]
for i in zip(*b):
 if(i.count(i[0])==len(i)):
  mn.append(i[0])
 
 else:
  break
print(''.join(mn))

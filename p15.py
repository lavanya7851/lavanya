nn=str(input())
s={}

for i in nn:
    if i not in s.keys():
        s[i]=nn.count(i)
print(max(s, key=s.get))

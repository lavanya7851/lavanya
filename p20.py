kk=input()
b='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
c=''
for i in kk:
  if i in b:
    t=b.index(i)
    t=t+3
    c=c+b[t]
print(c)

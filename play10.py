s=input()
s=s.split()
vi=s[0]
y=s[1]
c=0
i=0
while(i<len(vi) and c<2):
    if(vi[i]!=y[i]):
        c+=1
    i+=1
if(c==1 or c==0):
    print("yes")
else:
    print("no")


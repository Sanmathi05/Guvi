vihas,san=map(int,input().split())
t=[]
x=0
for m in range(vihas):
    t.append(list(map(int,input().split())))   
for m in range(vihas):
    for j in range(san-1):
        for k in range(j+1,san+1):
            if t[m][j:k]==[1]*len(t[m][j:k]):
                 if all(t[p+m][j:k]==[1]*len(t[p+m][j:k]) for p in range(len(t[m][j:k])-1)):
                     if len(t[m][j:k])>x:
                        x=len(t[m][j:k])
if len(t)==1 and len(t[0])==1 and t[0][0]==1:
    print(1)
for m in range(x):
    print(*[1]*x) 

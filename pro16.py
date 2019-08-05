sa=int(input())
us=list(map(int,input().split()))
q=[1]*sa
for i in range(sa):
    if i==0:
        if us[i]>us[i+1]:
            q[i]=q[i]+q[i+1]
    elif i>0:
        if us[i]>us[i-1]:
            q[i]=q[i]+q[i-1]
print(sum(q))

val=int(input())
b=[]
h=0
for i in range (0,val+1):
    h=abs((2**i)-val)
    b.append(h)
m=min(b)
print(m)

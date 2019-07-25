import math
no,z=map(int,input().split())
arr=[]
v=list(map(int,input().split()))
for n in range(0,z):
        c,d=map(int,input().split())
        arr.append([c,d])
for n in arr:
        q=n[0]-1
        p=n[1]-1
        print(math.gcd(v[q],v[p]))

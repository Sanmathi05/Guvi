no=int(input())
vs=list(map(int,input().split()))
vs.sort()
vs.reverse()
if vs[0]==0:
    print(0)
else:
    for z in vs:
        print(z,end='')

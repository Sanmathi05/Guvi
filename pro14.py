vihas,san=map(int,input().split())
vs=list(map(int,input().split()))
vihas=[]
vs.insert(0,0)
for y in range(san):
     vis=[]
     z=0
     hh,yy=map(int,input().split())
     for i in range(hh,yy+1):         
         z^=vs[i]     
     vihas.append(z)
for w in vihas:
     print(w)

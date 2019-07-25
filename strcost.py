p,q=map(str,input().split())
y=0
if len(p)>len(q):
	p,q=q,p
z=0
while z<len(p):
	  y+=(ord(q[z])-ord(p[z]))
	  z+=1
for z in range(z,len(q)):
	  y+=ord(q[z])-ord('p')+1
print(y)

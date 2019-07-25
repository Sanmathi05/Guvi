a,d=input().strip().split(" ")
d=int(d)
c=0
while c<len(a)-1 and d:
	if(a[c]>a[c+1]):
		d-=1
		a=a[:c]+a[c+1:]
		if(c!=0):
			c-=1
	else:
		c+=1
s=a[:len(a)-d]
print(s)
  

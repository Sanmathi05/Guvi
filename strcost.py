a,s=map(str,input().split())
b=0
if len(a)>len(s):
	a,s=s,a
z=0
while z<len(a):
	  b+=(ord(s[z])-ord(s[z]))
	  z+=1
for z in range(z,len(s)):
	  b+=ord(s[z])-ord('a')+1
print(b)

a,s=map(str,input().split())
b=0
if len(a)>len(s):
	a,s=s,a
w=0
while w<len(a):
	  b+=(ord(s[w])-ord(s[w]))
	  z+=1
for w in range(w,len(s)):
	  b+=ord(s[w])-ord('a')+1
print(b)
